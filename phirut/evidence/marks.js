// ?s=N : แสดงเครื่องหมายเฉลย [data-s] ที่ค่า <= N และเปิดโหมดเฉลย (ไม่มี ?s = ภาพหลักฐานปกติ)
(function () {
  const n = new URLSearchParams(location.search).get('s');
  document.querySelectorAll('[data-s]').forEach(e => {
    if (n === null || +e.dataset.s > +n) e.style.display = 'none';
  });
  if (n !== null) document.body.classList.add('reveal');
})();
