// main.js: dark mode toggle, active nav highlighting, smooth scroll
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('dark-toggle');
  const current = localStorage.getItem('naijajobs-theme');
  if (current === 'dark') document.body.classList.add('dark');

  toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    localStorage.setItem('naijajobs-theme', document.body.classList.contains('dark') ? 'dark' : 'light');
  });

  // smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      document.querySelector(a.getAttribute('href')).scrollIntoView({behavior:'smooth'});
    });
  });

  // Smooth hero transition on theme toggle
document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  const hero = document.querySelector('.hero');
  if (!hero) return;

  // Add a class to enable CSS transitions only after initial load
  setTimeout(() => hero.classList.add('hero-ready'), 120);

  // Optional: animate subtle parallax on mouse move for desktop
  if (window.matchMedia('(pointer:fine)').matches) {
    hero.addEventListener('mousemove', (e) => {
      const rect = hero.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      hero.style.setProperty('--hero-x', (x * 6).toFixed(2) + 'px');
      hero.style.setProperty('--hero-y', (y * 6).toFixed(2) + 'px');
    });
  }
});

  // active nav link highlight
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    if (link.href === location.href) link.classList.add('active');
  });
});
