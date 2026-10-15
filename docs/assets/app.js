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

      let commandSelected = false;
      if (!copied) {
        const command = button.closest('.command-row, .clone-command')?.querySelector('code');
        if (command) {
          const selection = window.getSelection();
          const range = document.createRange();
          range.selectNodeContents(command);
          selection.removeAllRanges();
          selection.addRange(range);
          commandSelected = true;
        }
      }

      button.textContent = copied ? 'Copied' : 'Select';
      if (toast) {
        toast.textContent = copied
          ? 'Command copied'
          : commandSelected
            ? 'Copy failed. Command selected — press ⌘C or Ctrl+C.'
            : 'Copy failed. Select the command and copy it manually.';
        toast.classList.add('show');
        clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => toast.classList.remove('show'), 1800);
      }
      setTimeout(() => { button.textContent = 'Copy'; }, 1800);
    });
  });

})();
