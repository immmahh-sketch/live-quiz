// Shared bits for one-off quiz scripts: LQ (assets/common.js run in a vm) and the quiz-api caller.
// The host password comes from the LQ_PASSWORD environment variable; nothing secret lives in this file.
//   import { LQ, api, uid } from 'C:/Users/GM/Documents/live-quiz/tools/lq.mjs';
import fs from 'node:fs'; import vm from 'node:vm'; import path from 'node:path'; import url from 'node:url';
const ROOT = path.join(path.dirname(url.fileURLToPath(import.meta.url)), '..');
const ctxv = { document: { addEventListener() {}, querySelector() { return null; }, querySelectorAll() { return []; }, createElement() { return { style: {}, setAttribute() {}, appendChild() {} }; }, head: { appendChild() {} } }, location: { href: 'https://letsquiz.uk/', search: '', pathname: '/' }, navigator: { userAgent: 'node' }, localStorage: { getItem() { return null; }, setItem() {}, removeItem() {} }, sessionStorage: { getItem() { return null; }, setItem() {}, removeItem() {} }, setTimeout, clearTimeout, setInterval, clearInterval, console, fetch, URLSearchParams, URL, crypto };
ctxv.window = ctxv; vm.createContext(ctxv); vm.runInContext(fs.readFileSync(path.join(ROOT, 'assets/common.js'), 'utf8'), ctxv);
export const LQ = ctxv.LQ;
const KEY = 'sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU';
export const api = async (action, body) => { for (let i = 0; i < 3; i++) { try { const r = await fetch('https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api', { method: 'POST', headers: { 'content-type': 'application/json', apikey: KEY, Authorization: 'Bearer ' + KEY }, body: JSON.stringify({ action, password: process.env.LQ_PASSWORD, ...body }) }); const d = await r.json(); if (d.error) throw new Error(d.error); return d; } catch (e) { if (i === 2) throw e; await new Promise((r) => setTimeout(r, 1500)); } } };
export const uid = (p) => p + '_' + Math.random().toString(36).slice(2, 10);
