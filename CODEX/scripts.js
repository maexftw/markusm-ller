const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function initNavigation() {
    const toggle = document.querySelector('.nav__toggle');
    const mobileMenu = document.querySelector('.nav__mobile');

    if (!toggle || !mobileMenu) return;

    toggle.addEventListener('click', () => {
        const expanded = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', String(!expanded));
        mobileMenu.classList.toggle('is-open', !expanded);
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            toggle.setAttribute('aria-expanded', 'false');
            mobileMenu.classList.remove('is-open');
        });
    });
}

function initCursor() {
    if (prefersReducedMotion) return;
    const blob = document.querySelector('.cursor-blob');
    if (!blob) return;

    let rafId;
    let targetX = window.innerWidth / 2;
    let targetY = window.innerHeight / 2;
    let currentX = targetX;
    let currentY = targetY;

    const lerp = (start, end, alpha) => start + (end - start) * alpha;

    function animate() {
        currentX = lerp(currentX, targetX, 0.15);
        currentY = lerp(currentY, targetY, 0.15);
        blob.style.transform = `translate(${currentX - 160}px, ${currentY - 160}px)`;
        rafId = requestAnimationFrame(animate);
    }

    window.addEventListener('pointermove', event => {
        targetX = event.clientX;
        targetY = event.clientY;
        if (!rafId) {
            blob.style.opacity = '0.55';
            animate();
        }
    });

    window.addEventListener('pointerdown', () => {
        blob.style.opacity = '0.8';
    });

    window.addEventListener('pointerup', () => {
        blob.style.opacity = '0.55';
    });

    window.addEventListener('blur', () => {
        cancelAnimationFrame(rafId);
        rafId = null;
        blob.style.opacity = '0';
    });

    window.addEventListener('focus', () => {
        blob.style.opacity = '0.55';
        if (!rafId) animate();
    });
}

function initRevealAnimations() {
    const elements = document.querySelectorAll('[data-reveal]');
    if (!elements.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.25,
        rootMargin: '0px 0px -10% 0px'
    });

    elements.forEach(el => observer.observe(el));
}

function initPartnersMarquee() {
    const track = document.querySelector('.partners__track');
    if (!track) return;
    const logos = Array.from(track.children);
    if (logos.length === 0) return;
    const cloneFragment = document.createDocumentFragment();
    logos.forEach(logo => {
        const clone = logo.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        cloneFragment.appendChild(clone);
    });
    track.appendChild(cloneFragment);
}

function initHeroInteractions() {
    if (prefersReducedMotion) return;
    const hero = document.querySelector('.hero');
    if (!hero) return;

    const rotateLayer = hero;
    let timeoutId;

    hero.addEventListener('pointermove', (event) => {
        const rect = hero.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
        const y = ((event.clientY - rect.top) / rect.height - 0.5) * 2;

        rotateLayer.style.setProperty('transform', `perspective(1400px) rotateX(${(-y * 3).toFixed(2)}deg) rotateY(${(x * 3).toFixed(2)}deg) scale3d(1.01, 1.01, 1)`);
        rotateLayer.style.setProperty('transition', 'transform 0.12s ease-out');

        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            rotateLayer.style.removeProperty('transform');
            rotateLayer.style.setProperty('transition', 'transform 0.6s ease');
        }, 120);
    });

    hero.addEventListener('pointerleave', () => {
        rotateLayer.style.removeProperty('transform');
        rotateLayer.style.setProperty('transition', 'transform 0.6s ease');
    });
}

window.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initCursor();
    initRevealAnimations();
    initPartnersMarquee();
    initHeroInteractions();
});
