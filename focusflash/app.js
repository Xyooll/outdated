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
  let lastSaveAt = 0;
  const wordMetrics = document.createElement('canvas').getContext('2d');

  const STORAGE_KEY = window.FocusFlashProfiles?.key('focusflash-state-v1') || 'focusflash-state-v1';

  function tokenize(text) {
    return text.trim().split(/\s+/).filter(Boolean).slice(0, 100000);
  }

  function focalIndex(word) {
    // Always center the focal LETTER, not surrounding punctuation.
    // For even letter counts, highlight the letter just left of center.
    const chars = [...word];
    const letters = [];
    for (let i = 0; i < chars.length; i++) {
      if (/[\p{L}\p{N}]/u.test(chars[i])) letters.push(i);
    }
    return letters.length ? letters[Math.floor((letters.length - 1) / 2)] :
      Math.max(0, Math.floor((chars.length - 1) / 2));
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

    const px = Math.max(16, Math.min(120, Number(els.fontSize.value) || 48));
    const wordNode = els.wordStage.querySelector('.word');
    const stageWidth = Math.max(100, els.wordStage.clientWidth || 240);
    let fitted = px;
    if (wordMetrics && wordNode) {
      // Focus letter stays centered, so reserve equal room for both halves.
      // Fit long words without simply clipping them in a narrow portrait frame.
      wordMetrics.font = '700 ' + px + 'px ' + getComputedStyle(wordNode).fontFamily;
      const half = Math.max(
        wordMetrics.measureText(parts.left).width,
        wordMetrics.measureText(parts.right).width
      );
      const middle = wordMetrics.measureText(parts.focus).width;
      const needed = half * 2 + middle + 22;
      if (needed > stageWidth) fitted = Math.max(10, Math.floor(px * (stageWidth - 8) / needed));
    }
    if (wordNode) wordNode.style.fontSize = fitted + 'px';
    els.fontSizeValue.textContent = px + ' px';
    const videoLabel = $('studioScaleValue');
    if (videoLabel) videoLabel.textContent = px + ' px';
    const hint = $('fontFitHint');
    if (hint) hint.textContent = fitted < px ?
      'This word is displayed at ' + fitted + ' px to fit the preview. Your chosen size is ' + px + ' px.' :
      'Preview and video use the same size. Longer words shrink automatically to fit.';
    els.wpmValue.textContent = `${wpm} WPM`;

    els.backBtn.disabled = index <= 0;
    els.nextBtn.disabled = index >= words.length - 1;

    saveState();
    // Update the editor timeline without forcing it to re-tokenize on every frame.
    document.dispatchEvent(new CustomEvent('focusflash:render',{
      detail:{index,total:words.length,wpm}
    }));
  }

  function stop() {
    playing = false;
    if (timer) clearTimeout(timer);
    timer = null;
    els.playBtn.textContent = '▶ Play';
    window.FocusFlashStudio?.stopReaderUndertone?.();
    window.FocusFlashTones?.stopReader?.();
    saveState(true);
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
    window.FocusFlashStudio?.startReaderUndertone?.(index);
    window.FocusFlashTones?.startReader?.();
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

  function saveState(force=false) {
    // Avoid serializing long passages to localStorage for every flashed word.
    const now=Date.now();
    if(!force&&now-lastSaveAt<1500)return;
    lastSaveAt=now;
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
      if (Number.isFinite(s.fontSize)) els.fontSize.value = String(Math.max(16, Math.min(120, s.fontSize)));
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

  els.fontSize.addEventListener('input', () => {
    render();
    saveState(true);
  });
  // Make the word fit adjust when the phone rotates or the canvas format changes.
  if ('ResizeObserver' in window)
    new ResizeObserver(() => render()).observe(els.wordStage);
  els.punctuationPause.addEventListener('change', saveState);
  els.longWordPause.addEventListener('change', saveState);
  els.sourceText.addEventListener('input', () => saveState(true));

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

  window.FocusFlashReader = {
    isPlaying:()=>playing,currentIndex:()=>index,
    pause:()=>{if(playing)stop();},persist:()=>saveState(true)
  };
  window.FocusFlashProfiles?.mount?.();
  restoreState();
  loadText(false);
  if(window.FocusFlashTones)window.FocusFlashTones.mount();
  if(window.FocusFlashSpatial)window.FocusFlashSpatial.mount();
  if(window.FocusFlashStudio)window.FocusFlashStudio.mount();
  if(window.FocusFlashEditor)window.FocusFlashEditor.mount();
})();
