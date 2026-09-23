/* A built-in sample quiz so the game can be tried before any quiz is saved: host.html?quiz=demo */
window.DEMO_QUIZ = {
  id: 'demo',
  title: 'Demo quiz',
  settings: { maxPoints: 1000, minPoints: 500, defaultTime: 20, showAnswersOnPhones: true },
  questions: [
    { id: 'd1', type: 'choice', text: 'Which planet is closest to the Sun?', time: 15, media: { kind: 'none' },
      options: [{ id: 'd1a', text: 'Venus' }, { id: 'd1b', text: 'Mercury' }, { id: 'd1c', text: 'Mars' }, { id: 'd1d', text: 'Earth' }], correct: 'd1b' },
    { id: 'd2', type: 'choice', text: 'Which city is this landmark in?', time: 15,
      media: { kind: 'image', url: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a0/Sydney_Australia._%2821339175489%29.jpg/960px-Sydney_Australia._%2821339175489%29.jpg', credit: 'Wikipedia: Sydney Opera House' },
      options: [{ id: 'd2a', text: 'Melbourne' }, { id: 'd2b', text: 'Auckland' }, { id: 'd2c', text: 'Sydney' }, { id: 'd2d', text: 'Cape Town' }], correct: 'd2c' },
    { id: 'd3', type: 'text', text: 'Who painted the Mona Lisa?', time: 20, media: { kind: 'none' }, answers: ['Leonardo da Vinci', 'Da Vinci', 'Leonardo'], ai: true },
    { id: 'd4', type: 'order', text: 'Put these in order, earliest first', time: 30, media: { kind: 'none' }, hint: 'earliest to latest', partial: true,
      items: [{ id: 'd4a', text: 'First Moon landing' }, { id: 'd4b', text: 'Fall of the Berlin Wall' }, { id: 'd4c', text: 'Launch of the iPhone' }, { id: 'd4d', text: 'London Olympics' }] },
    { id: 'd5', type: 'match', text: 'Match the breed to the dog', time: 40, media: { kind: 'none' }, partial: true,
      pairs: [
        { id: 'd5a', left: 'Labrador', right: { kind: 'image', value: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock_%282175262184%29.jpg/960px-Labrador_on_Quantock_%282175262184%29.jpg' } },
        { id: 'd5b', left: 'Dalmatian', right: { kind: 'image', value: 'https://upload.wikimedia.org/wikipedia/commons/6/68/Sun_Dog_Dalmatian.jpg' } },
        { id: 'd5c', left: 'Pug', right: { kind: 'image', value: 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f3/Mops-duke-mopszucht-vom-maegdebrunnen.jpg/960px-Mops-duke-mopszucht-vom-maegdebrunnen.jpg' } },
        { id: 'd5d', left: 'Border Collie', right: { kind: 'image', value: 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Border_Collie_600.jpg' } },
      ] },
    { id: 'd6', type: 'pin', text: 'Drop the pin on Namibia', time: 20, place: 'Namibia',
      media: { kind: 'image', url: 'https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg', credit: 'Wikimedia Commons' },
      pin: { x: (17 + 180) / 360, y: (90 - -22) / 180 }, radiusFull: 0.02, radiusZero: 0.08 },
    { id: 'd7', type: 'text', text: 'Name the band', time: 25,
      media: { kind: 'youtube', url: 'https://www.youtube.com/watch?v=fJ9rUzIMcZQ', videoId: 'fJ9rUzIMcZQ', start: 0 },
      answers: ['Queen'], ai: true },
  ],
};
