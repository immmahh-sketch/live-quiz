// The car screen: one CarPlay list that is redrawn whenever the game's state changes. Tapping a row sends the same thing a tap on the
// phone would. Only used when the app is built with CarPlay on (CARPLAY=1) and Apple has granted the entitlement.
import { buildRows, GameState, Act } from './model';

type Send = (k: string, v: unknown, extra?: Record<string, unknown>) => void;

export function startCarPlay(send: Send) {
  // required here, not at the top, so a build without CarPlay never loads the native module
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const { CarPlay, ListTemplate } = require('@g4rb4g3/react-native-carplay');
  let state: GameState | null = null;
  let openRow: number | null = null; // while picking a box: the category whose boxes are showing
  let template: any = null;
  let acts: (Act | undefined)[] = [];
  let cap = 12; // some cars show fewer rows than others; asked from the car when it connects

  const sections = () => {
    const { title, rows } = buildRows(state, openRow);
    const shown = rows.slice(0, cap);
    acts = shown.map((r) => r.act);
    return [{ header: title, items: shown.map((r, i) => ({ id: String(i), text: r.text, detailText: r.detail })) }];
  };
  const refresh = () => { try { template?.updateSections(sections()); } catch (e) { /* the car may have gone */ } };

  const onConnect = () => {
    template = new ListTemplate({
      title: 'Box Clever',
      sections: sections(),
      onItemSelect: async ({ id }: { id?: string }) => {
        const a = acts[Number(id)];
        if (!a) return;
        if ('row' in a) { openRow = a.row; refresh(); } else { const [k, v, extra] = a.send; send(k, v, extra); }
      },
    });
    CarPlay.setRootTemplate(template, false);
    template.getMaximumListItemCount?.().then((n: number) => { if (n > 3) { cap = n; refresh(); } }).catch(() => {});
  };
  const onDisconnect = () => { template = null; };
  CarPlay.registerOnConnect(onConnect);
  CarPlay.registerOnDisconnect(onDisconnect);
  if (CarPlay.connected) onConnect();

  return {
    setState(s: GameState) { state = s; if (s.needs !== 'pick') openRow = null; refresh(); },
    stop() { CarPlay.unregisterOnConnect(onConnect); CarPlay.unregisterOnDisconnect(onDisconnect); },
  };
}
