#!/usr/bin/env python3
# Script to generate properly formatted KOST subpages with correct navigation

import os

# Define the base template with desktop dropdown navigation
def get_template(page_name, description, title, eyebrow, h1, intro1, intro2, sections):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
    <link rel="stylesheet" href="../css/theme.css">
    <style>
        .scroll-reveal {{
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }}
        .scroll-reveal.active {{
            opacity: 1;
            transform: translateY(0);
        }}
        .mobile-menu {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px);
            z-index: 9998;
            padding: 6rem 2rem 2rem;
            opacity: 0;
            transform: translateY(-20px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }}
        .mobile-menu.active {{
            display: block;
            opacity: 1;
            transform: translateY(0);
        }}
        .mobile-menu-link {{
            display: block;
            font-size: 2rem;
            font-weight: 600;
            color: var(--foreground, #1d1d1f);
            text-decoration: none;
            padding: 1.5rem 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            transition: color 0.2s ease;
        }}
        .mobile-menu-link:hover {{
            color: var(--kost-red, #FA0016);
        }}
        .mobile-dropdown {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }}
        .mobile-dropdown.active {{
            max-height: 500px;
        }}
        .mobile-dropdown-link {{
            display: block;
            font-size: 1.125rem;
            font-weight: 400;
            color: var(--muted-foreground, #86868b);
            text-decoration: none;
            padding: 1rem 0 1rem 2rem;
            transition: color 0.2s ease;
        }}
        .mobile-dropdown-link:hover {{
            color: var(--kost-red, #FA0016);
        }}
        .mobile-dropdown-toggle {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            cursor: pointer;
        }}
        .mobile-dropdown-toggle i {{
            transition: transform 0.3s ease;
        }}
        .mobile-dropdown-toggle.active i {{
            transform: rotate(180deg);
        }}
    </style>
</head>
<body>

    <!-- NAVIGATION -->
    <nav class="nav-apple" id="mainNav">
        <div class="container">
            <div class="flex justify-between items-center">
                <a href="../index.html" class="text-xl font-semibold" style="color: var(--foreground, #1d1d1f); text-decoration: none;" aria-label="KOST Sicherheitstechnik Homepage">
                    KOST<span style="color: var(--kost-red, #FA0016);">.</span>
                </a>

                <div class="hidden md:flex items-center gap-8">
                    <a href="../index.html" class="nav-link-apple">Startseite</a>
                    <div class="relative group">
                        <a href="../index.html#services" class="nav-link-apple flex items-center gap-1">
                            Leistungen
                            <i data-lucide="chevron-down" style="width: 16px; height: 16px;"></i>
                        </a>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-white rounded-xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300" style="border: 1px solid rgba(0,0,0,0.08);">
                            <a href="videoueberwachung.html" class="block px-4 py-3 text-sm hover:bg-gray-50 transition-colors" style="color: var(--foreground, #1d1d1f); text-decoration: none;">Videoüberwachung</a>
                            <a href="alarmanlagen.html" class="block px-4 py-3 text-sm hover:bg-gray-50 transition-colors" style="color: var(--foreground, #1d1d1f); text-decoration: none;">Alarmanlagen</a>
                            <a href="zutrittskontrolle.html" class="block px-4 py-3 text-sm hover:bg-gray-50 transition-colors" style="color: var(--foreground, #1d1d1f); text-decoration: none;">Zutrittskontrolle</a>
                            <a href="briefkasten.html" class="block px-4 py-3 text-sm hover:bg-gray-50 transition-colors" style="color: var(--foreground, #1d1d1f); text-decoration: none;">Briefkastenanlagen</a>
                            <a href="mechanische-sicherung.html" class="block px-4 py-3 text-sm hover:bg-gray-50 transition-colors" style="color: var(--foreground, #1d1d1f); text-decoration: none; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px;">Mechanische Sicherung</a>
                        </div>
                    </div>
                    <a href="../index.html#about" class="nav-link-apple">Über uns</a>
                    <a href="../index.html#contact" class="nav-link-apple">Kontakt</a>
                </div>

                <button class="md:hidden" id="mobileToggle" aria-label="Navigation öffnen" aria-expanded="false" style="background: none; border: none; cursor: pointer;">
                    <i data-lucide="menu" style="width: 24px; height: 24px; color: var(--foreground, #1d1d1f);"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- MOBILE MENU -->
    <div class="mobile-menu" id="mobileMenu">
        <button id="mobileClose" aria-label="Navigation schließen" style="position: absolute; top: 1.5rem; right: 2rem; background: none; border: none; cursor: pointer;">
            <i data-lucide="x" style="width: 32px; height: 32px; color: var(--foreground, #1d1d1f);"></i>
        </button>
        <nav>
            <a href="../index.html" class="mobile-menu-link">Startseite</a>
            <div>
                <div class="mobile-menu-link mobile-dropdown-toggle" id="mobileDropdownToggle">
                    <span>Leistungen</span>
                    <i data-lucide="chevron-down" style="width: 24px; height: 24px;"></i>
                </div>
                <div class="mobile-dropdown" id="mobileDropdown">
                    <a href="videoueberwachung.html" class="mobile-dropdown-link">Videoüberwachung</a>
                    <a href="alarmanlagen.html" class="mobile-dropdown-link">Alarmanlagen</a>
                    <a href="zutrittskontrolle.html" class="mobile-dropdown-link">Zutrittskontrolle</a>
                    <a href="briefkasten.html" class="mobile-dropdown-link">Briefkastenanlagen</a>
                    <a href="mechanische-sicherung.html" class="mobile-dropdown-link">Mechanische Sicherung</a>
                </div>
            </div>
            <a href="../index.html#about" class="mobile-menu-link">Über uns</a>
            <a href="../index.html#contact" class="mobile-menu-link">Kontakt</a>
        </nav>
    </div>

    <!-- HERO SECTION -->
    <section class="section-apple" style="padding-top: 6rem; padding-bottom: 4rem; background: linear-gradient(180deg, #fff 0%, #f5f5f7 100%);">
        <div class="container">
            <div class="max-w-4xl mx-auto text-center">
                <div class="hero-eyebrow mb-md">{eyebrow}</div>
                <h1 class="display-xl mb-lg">{h1}</h1>
                <p class="body-lg" style="max-width: 680px; margin: 0 auto;">{intro1}</p>
            </div>
        </div>
    </section>

    <!-- INTRO SECTION -->
    <section class="section-apple">
        <div class="max-w-4xl mx-auto text-center scroll-reveal">
            {intro2}
        </div>
    </section>

    {sections}

    <!-- FOOTER -->
    <footer class="footer-apple">
        <div class="footer-grid">
            <div class="footer-section">
                <h4>Leistungen</h4>
                <a href="videoueberwachung.html" class="footer-link">Videoüberwachung</a>
                <a href="alarmanlagen.html" class="footer-link">Alarmanlagen</a>
                <a href="zutrittskontrolle.html" class="footer-link">Zutrittskontrolle</a>
                <a href="briefkasten.html" class="footer-link">Briefkastenanlagen</a>
                <a href="mechanische-sicherung.html" class="footer-link">Mechanische Sicherung</a>
            </div>
            <div class="footer-section">
                <h4>Unternehmen</h4>
                <a href="../index.html#about" class="footer-link">Über uns</a>
                <a href="../index.html#contact" class="footer-link">Kontakt</a>
            </div>
            <div class="footer-section">
                <h4>Kontakt</h4>
                <p class="footer-link">Hermannstr. 162a<br>44263 Dortmund</p>
                <p class="footer-link">Tel: 0231 / 98 98 351</p>
            </div>
            <div class="footer-section">
                <h4>Rechtliches</h4>
                <a href="#impressum" class="footer-link">Impressum</a>
                <a href="#datenschutz" class="footer-link">Datenschutz</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2025 KOST Sicherheitstechnik</p>
        </div>
    </footer>

    <!-- SCRIPTS -->
    <script>
        // Initialize Lucide Icons
        lucide.createIcons();

        // Navigation scroll effect
        const nav = document.getElementById('mainNav');
        window.addEventListener('scroll', () => {{
            nav.classList.toggle('scrolled', window.pageYOffset > 50);
        }});

        // Scroll reveal animation
        const observerOptions = {{
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        }};
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('active');
                }}
            }});
        }}, observerOptions);
        document.querySelectorAll('.scroll-reveal').forEach(el => observer.observe(el));

        // Mobile menu toggle
        const mobileToggle = document.getElementById('mobileToggle');
        const mobileMenu = document.getElementById('mobileMenu');
        const mobileClose = document.getElementById('mobileClose');

        if (mobileToggle && mobileMenu) {{
            mobileToggle.addEventListener('click', () => {{
                mobileMenu.classList.add('active');
                mobileToggle.setAttribute('aria-expanded', 'true');
                document.body.style.overflow = 'hidden';
            }});
        }}

        if (mobileClose && mobileMenu) {{
            mobileClose.addEventListener('click', () => {{
                mobileMenu.classList.remove('active');
                mobileToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }});
        }}

        // Mobile dropdown toggle
        const mobileDropdownToggle = document.getElementById('mobileDropdownToggle');
        const mobileDropdown = document.getElementById('mobileDropdown');

        if (mobileDropdownToggle && mobileDropdown) {{
            mobileDropdownToggle.addEventListener('click', () => {{
                mobileDropdown.classList.toggle('active');
                mobileDropdownToggle.classList.toggle('active');
            }});
        }}

        // Close mobile menu when clicking on a link
        document.querySelectorAll('.mobile-menu-link:not(.mobile-dropdown-toggle), .mobile-dropdown-link').forEach(link => {{
            link.addEventListener('click', () => {{
                if (mobileMenu) {{
                    mobileMenu.classList.remove('active');
                    mobileToggle.setAttribute('aria-expanded', 'false');
                    document.body.style.overflow = '';
                }}
            }});
        }});
    </script>
</body>
</html>"""

print("Template generation complete - ready for use")
