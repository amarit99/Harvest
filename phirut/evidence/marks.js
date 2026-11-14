// ?s=N : เปิดโหมดเฉลย แสดงเครื่องหมายที่ค่า <= N (ไม่มี ?s = ภาพหลักฐานปกติ)
//  - [data-s]  : องค์ประกอบที่วางตำแหน่งเอง (โน้ต/วงรีใน svg.marks)
//  - [data-hl] : วงรีวาดอัตโนมัติรอบข้อความนั้น (วงอยู่ใน container ที่มี data-markroot หรือ .paper)
(function () {
  const n = new URLSearchParams(location.search).get('s');
  document.querySelectorAll('[data-s]').forEach(e => {
    if (n === null || +e.dataset.s > +n) e.style.display = 'none';
  });
  if (n === null) return;
  document.body.classList.add('reveal');
  document.querySelectorAll('[data-hl]').forEach((el, i) => {
    if (+el.dataset.hl > +n) return;
    const root = el.closest('[data-markroot]') || el.closest('.paper');
    let x = 0, y = 0, p = el;
    while (p && p !== root) { x += p.offsetLeft; y += p.offsetTop; p = p.offsetParent; }
    const w = el.offsetWidth, h = el.offsetHeight, pad = +(el.dataset.pad || 26);
    let svg = root.querySelector(':scope > svg.marks.auto');
    if (!svg) {
      svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('class', 'marks auto');
      svg.style.overflow = 'visible';
      root.appendChild(svg);
    }
    const e = document.createElementNS('http://www.w3.org/2000/svg', 'ellipse');
    e.setAttribute('cx', x + w/2); e.setAttribute('cy', y + h/2);
    e.setAttribute('rx', w/2 + pad); e.setAttribute('ry', h/2 + pad*0.55);
    e.setAttribute('transform', `rotate(${i % 2 ? 1.5 : -1.5} ${x + w/2} ${y + h/2})`);
    svg.appendChild(e);
  });
})();
