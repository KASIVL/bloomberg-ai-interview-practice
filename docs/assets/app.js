(() => {
  const toast = document.querySelector('.toast');
  let toastTimeout;

  document.querySelectorAll('[data-copy]').forEach((button) => {
    button.addEventListener('click', async () => {
      const value = button.dataset.copy;
      let copied = false;

      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(value);
          copied = true;
        }
      } catch (_) {}

      if (!copied) {
        const field = document.createElement('textarea');
        field.value = value;
        field.setAttribute('readonly', '');
        field.style.position = 'fixed';
        field.style.left = '-9999px';
        document.body.append(field);
        field.select();
        copied = document.execCommand('copy');
        field.remove();
      }

      button.textContent = copied ? 'Copied' : 'Select';
      if (toast) {
        toast.textContent = copied ? 'Command copied' : 'Select the command to copy it';
        toast.classList.add('show');
        clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => toast.classList.remove('show'), 1800);
      }
      setTimeout(() => { button.textContent = 'Copy'; }, 1800);
    });
  });

  const readouts = [...document.querySelectorAll('[data-timer]')];
  if (!readouts.length) return;

  let remaining = 600;
  let interval = null;
  const render = () => {
    const minutes = Math.floor(remaining / 60).toString().padStart(2, '0');
    const seconds = (remaining % 60).toString().padStart(2, '0');
    readouts.forEach((node) => { node.textContent = `${minutes}:${seconds}`; });
  };

  document.querySelectorAll('[data-timer-action]').forEach((button) => {
    button.addEventListener('click', () => {
      const action = button.dataset.timerAction;
      if (action === 'start' && interval === null && remaining > 0) {
        interval = setInterval(() => {
          remaining -= 1;
          render();
          if (remaining <= 0) {
            clearInterval(interval);
            interval = null;
          }
        }, 1000);
      } else if (action === 'pause' && interval !== null) {
        clearInterval(interval);
        interval = null;
      } else if (action === 'reset') {
        if (interval !== null) clearInterval(interval);
        interval = null;
        remaining = 600;
        render();
      }
    });
  });

  render();
})();
