(() => {
  const $ = (id) => document.getElementById(id);
  const els = {
    installBtn: $('installBtn'),
    progressText: $('progressText'),
    timeText: $('timeText'),
    wordStage: $('wordStage'),
    leftPart: $('leftPart'),
    focusPart: $('focusPart'),
    rightPart: $('rightPart'),
    backBtn: $('backBtn'),
    playBtn: $('playBtn'),
    nextBtn: $('nextBtn'),
    progressRange: $('progressRange'),
    wpm: $('wpm'),
    wpmValue: $('wpmValue'),
    punctuationPause: $('punctuationPause'),
    longWordPause: $('longWordPause'),
    fontSize: $('fontSize'),
    fontSizeValue: $('fontSizeValue'),
    sourceText: $('sourceText'),
    loadBtn: $('loadBtn'),
    resetBtn: $('resetBtn'),
    clearBtn: $('clearBtn')
  };

  let words = [];
  let index = 0;
  let timer = null;
  let playing = false;
  let deferredInstall = null;
  let touchStartX = null;

  const STORAGE_KEY = 'focusflash-state-v1';

  function tokenize(text) {
    return text.trim().split(/\s+/).filter(Boolean).slice(0, 100000);
  }

  function focalIndex(word) {
    const n = [...word].length;
    if (n <= 1) return 0;
    if (n <= 5) return Math.max(0, Math.floor((n - 1) * 0.40));
    if (n <= 9) return Math.max(0, Math.floor((n - 1) * 0.38));
    return Math.max(0, Math.floor((n - 1) * 0.35));
  }

  function splitWord(word) {
    const chars = [...word];
    const fi = Math.min(focalIndex(word), Math.max(0, chars.length - 1));
    return {
      left: chars.slice(0, fi).join(''),
      focus: chars[fi] || ' ',
      right: chars.slice(fi + 1).join('')
    };
  }

  function delayFor(word) {
    const wpm = Math.max(60, Math.min(2000, Number(els.wpm.value) || 300));
    let ms = 60000 / wpm;

    if (els.punctuationPause.checked) {
      if (/[.!?][”’"'')\]]*$/.test(word)) ms *= 1.8;
      else if (/[,;:][”’"'')\]]*$/.test(word)) ms *= 1.35;
    }

    if (els.longWordPause.checked && [...word].length >= 12) {
      ms *= 1.2;
    }
    return Math.max(30, ms);
  }

  function render() {
    const word = words[index] || 'Ready';
    const parts = splitWord(word);
    els.leftPart.textContent = parts.left;
    els.focusPart.textContent = parts.focus;
    els.rightPart.textContent = parts.right;

    const total = Math.max(words.length, 1);
    els.progressText.textContent = `Word ${Math.min(index + 1, total)} of ${total}`;
    els.progressRange.max = Math.max(0, total - 1);
    els.progressRange.value = Math.min(index, total - 1);

    const wpm = Number(els.wpm.value) || 300;
    const remaining = Math.max(0, total - index - 1);
    const sec = Math.ceil((remaining / wpm) * 60);
    els.timeText.textContent = sec >= 60 ? `~${Math.ceil(sec / 60)} min left` : `~${sec} sec left`;

    const px = Number(els.fontSize.value) || 64;
    document.querySelector('.word').style.fontSize = `${px}px`;
    els.fontSizeValue.textContent = `${px} px`;
    els.wpmValue.textContent = `${wpm} WPM`;

    els.backBtn.disabled = index <= 0;
    els.nextBtn.disabled = index >= words.length - 1;

    saveState();
  }

  function stop() {
    playing = false;
    if (timer) clearTimeout(timer);
    timer = null;
    els.playBtn.textContent = '▶ Play';
    window.FocusFlashStudio?.stopReaderUndertone?.();
  }

  function tick() {
    if (!playing) return;
    render();
    const current = words[index];
    if (index >= words.length - 1) {
      timer = setTimeout(stop, delayFor(current));
      return;
    }
    timer = setTimeout(() => {
      index += 1;
      tick();
    }, delayFor(current));
  }

  function play() {
    if (!words.length) loadText();
    if (index >= words.length - 1 && words.length > 1) index = 0;
    playing = true;
    els.playBtn.textContent = '❚❚ Pause';
    tick();
  }

  function togglePlay() {
    playing ? stop() : play();
  }

  function loadText(resetIndex = true) {
    const next = tokenize(els.sourceText.value);
    words = next.length ? next : ['Ready'];
    if (resetIndex) index = 0;
    index = Math.min(index, words.length - 1);
    stop();
    render();
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        text: els.sourceText.value,
        index,
        wpm: Number(els.wpm.value),
        punctuationPause: els.punctuationPause.checked,
        longWordPause: els.longWordPause.checked,
        fontSize: Number(els.fontSize.value)
      }));
    } catch (_) {}
  }

  function restoreState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return false;
      const s = JSON.parse(raw);
      if (typeof s.text === 'string') els.sourceText.value = s.text;
      if (Number.isFinite(s.wpm)) els.wpm.value = String(Math.max(60, Math.min(2000, s.wpm)));
      if (typeof s.punctuationPause === 'boolean') els.punctuationPause.checked = s.punctuationPause;
      if (typeof s.longWordPause === 'boolean') els.longWordPause.checked = s.longWordPause;
      if (Number.isFinite(s.fontSize)) els.fontSize.value = String(Math.max(32, Math.min(96, s.fontSize)));
      words = tokenize(els.sourceText.value);
      if (!words.length) words = ['Ready'];
      index = Math.max(0, Math.min(Number.isFinite(s.index) ? s.index : 0, words.length - 1));
      return true;
    } catch (_) {
      return false;
    }
  }

  els.playBtn.addEventListener('click', togglePlay);
  els.wordStage.addEventListener('click', togglePlay);
  els.backBtn.addEventListener('click', () => { stop(); index = Math.max(0, index - 1); render(); });
  els.nextBtn.addEventListener('click', () => { stop(); index = Math.min(words.length - 1, index + 1); render(); });
  els.loadBtn.addEventListener('click', () => loadText(true));
  els.resetBtn.addEventListener('click', () => { stop(); index = 0; render(); });
  els.clearBtn.addEventListener('click', () => {
    stop();
    els.sourceText.value = '';
    words = ['Ready'];
    index = 0;
    render();
    els.sourceText.focus();
  });

  els.wpm.addEventListener('input', () => {
    els.wpmValue.textContent = `${els.wpm.value} WPM`;
    if (playing) {
      if (timer) clearTimeout(timer);
      timer = setTimeout(() => {
        index = Math.min(index + 1, words.length - 1);
        tick();
      }, delayFor(words[index] || ''));
    }
    saveState();
  });

  els.fontSize.addEventListener('input', render);
  els.punctuationPause.addEventListener('change', saveState);
  els.longWordPause.addEventListener('change', saveState);
  els.sourceText.addEventListener('input', saveState);

  els.progressRange.addEventListener('input', () => {
    stop();
    index = Number(els.progressRange.value) || 0;
    render();
  });

  els.wordStage.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0]?.clientX ?? null;
  }, {passive:true});

  els.wordStage.addEventListener('touchend', (e) => {
    if (touchStartX == null) return;
    const x = e.changedTouches[0]?.clientX ?? touchStartX;
    const dx = x - touchStartX;
    touchStartX = null;
    if (Math.abs(dx) < 50) return;
    stop();
    if (dx < 0) index = Math.min(words.length - 1, index + 1);
    else index = Math.max(0, index - 1);
    render();
  }, {passive:true});

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredInstall = e;
    els.installBtn.classList.remove('hidden');
  });

  els.installBtn.addEventListener('click', async () => {
    if (!deferredInstall) return;
    deferredInstall.prompt();
    try { await deferredInstall.userChoice; } catch (_) {}
    deferredInstall = null;
    els.installBtn.classList.add('hidden');
  });

  window.addEventListener('appinstalled', () => {
    deferredInstall = null;
    els.installBtn.classList.add('hidden');
  });

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('./service-worker.js').catch(() => {});
  }

  restoreState();
  loadText(false);
  if (window.FocusFlashStudio) window.FocusFlashStudio.mount();
})();
