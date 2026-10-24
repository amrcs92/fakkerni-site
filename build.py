"""Builds the Fakkerni website (English at /, Arabic at /ar/) from one template.

Run: python build.py   (writes index.html, privacy.html, ar/index.html, ar/privacy.html)
Policy texts live in content/privacy.en.html and content/privacy.ar.html.
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = "amrcs92/fakkerni-site"
DOWNLOAD = f"https://github.com/{REPO}/releases/latest/download/fakkerni.apk"
RELEASES = f"https://github.com/{REPO}/releases"
CONTACT = "amrcs1992@gmail.com"

ICONS = {
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    "speak": '<path d="M5 19.5 6.3 16A7.5 7.5 0 1 1 9 18.6z"/><path d="M9.5 10.5v2M12 9v5M14.5 10.5v2"/>',
    "pill": '<rect x="3.5" y="8.5" width="17" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="m9.2 9.2 5.6 5.6"/>',
    "cloud": '<path d="M7 18.5h10.5a4 4 0 0 0 .5-8 6 6 0 0 0-11.5 1.5A3.3 3.3 0 0 0 7 18.5z"/><path d="m9.5 14 2 2 3.5-3.5"/>',
    "power": '<path d="M12 3v8"/><path d="M6.3 7.3a8 8 0 1 0 11.4 0"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "download": '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/>',
    "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
}


def icon(name):
    return (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
    )


T = {
    "en": {
        "dir": "ltr",
        "title": "Fakkerni · Alarms, reminders and medication for Android",
        "desc": "Fakkerni is a free Arabic and English alarm, reminder and medication app for Android. No account, no ads, no tracking.",
        "nav": ["Features", "Screenshots", "Install", "Privacy"],
        "other_lang": "العربية",
        "download": "Download",
        "eyebrow": "Free for Android · In testing",
        "h1": "Everything that matters, on time",
        "lead": "Fakkerni (<bdi>فكّرني</bdi>, “remind me”) rings your reminders and medicine doses on time, even offline and right after a restart. Made Arabic first, with full English.",
        "cta": "Download for Android",
        "cta2": "See screenshots",
        "meta": "Android 8.0 or later · Free · About 60 MB",
        "trust": ["No account", "No ads", "No tracking", "Works offline", "Arabic and English"],
        "features_h": "Built to ring, every time",
        "features_p": "Reminders and medicines on alarms that keep working when the app is closed, the phone is asleep, or it has just restarted.",
        "features": [
            ("bell", "Alarms that ring", "Full-screen alarms over the lock screen, and over other apps while you use the phone, with snooze, early warnings and repeats from every few hours to every year."),
            ("speak", "Hear the title", "The reminder is spoken aloud in its own language, Arabic or English, once or every few seconds."),
            ("pill", "Medication made simple", "Each dose has its own alarm: taken, later or skipped. Stock tracking, refill alerts and a monthly history."),
            ("cloud", "Backups in your Drive", "Back up to a “Fakkerni backups” folder in your own Google Drive or a folder on your phone, with optional password encryption."),
            ("power", "Reliable after a restart", "Alarms ring even after the phone restarts, before you unlock it, and Fakkerni warns you if a battery saver holds it back."),
            ("globe", "Arabic first", "Right-to-left layout, Arabic digits and plurals, Saturday-first weeks, light and dark themes."),
        ],
        "gallery_h": "A closer look",
        "gallery_p": "Five main screens, in light and dark.",
        "light": "Light",
        "dark": "Dark",
        "shots": [("home", "Reminders"), ("edit", "Edit reminder"), ("medication", "Medication"), ("settings", "Settings"), ("backup", "Backup")],
        "install_h": "Install in a minute",
        "install_p": "Fakkerni isn't on Google Play yet. Download the APK and install it directly.",
        "card_h": "Fakkerni for Android",
        "card_p": "The latest version, ready to install.",
        "facts": ["Version", "Size", "Requires"],
        "requires": "Android 8.0+",
        "checksum": "SHA-256",
        "steps": [
            ("Download the APK", "Tap Download on your Android phone. The file is called fakkerni.apk."),
            ("Allow the install", "Open the file. If Android asks, allow installing apps from your browser or file manager."),
            ("Open Fakkerni", "Follow the short setup: language, notifications and alarm permissions. Allow “Show alarms over other apps” so alarms take the whole screen even while you use the phone. Already have a backup? Choose “I have a backup, restore”."),
        ],
        "note": "Google Play Protect may warn that the app comes from an unknown developer. That's because Fakkerni isn't on Google Play yet. Tap “More details” › “Install anyway”.",
        "privacy_h": "Private by design",
        "privacy_p": "Your reminders and medicines are personal. Fakkerni keeps them on your phone, and a backup goes only where you choose.",
        "privacy_link": "Read the privacy policy",
        "checks": [
            "No account and no sign-up",
            "No servers, analytics or ads",
            "Data stays on your phone",
            "Optional backups to your own Google Drive or a folder, encrypted if you like",
        ],
        "faq_h": "Questions",
        "faq": [
            ("Is Fakkerni free?", "Yes. No ads, no subscriptions and no in-app purchases."),
            ("Does it work without internet?", "Yes. Alarms, reminders and medication work fully offline. Internet is only used if you back up to Google Drive."),
            ("Where are my backups?", "Wherever you choose: a “Fakkerni backups” folder in your own Google Drive, a folder on your phone, or inside the app. You can encrypt them with a password."),
            ("Why isn't it on Google Play?", "Fakkerni is still being tested. It will come to Google Play later; until then you can install the APK from this page."),
            ("Which phones are supported?", "Android 8.0 or later. Some brands limit apps in the background; Fakkerni's setup shows how to keep alarms on time on your phone."),
            ("Why does an alarm show only as a banner?", "While you use your phone, Android shows alarms as a banner unless the app may display over other apps. Turn on Settings › Permissions › “Show alarms over other apps” in Fakkerni, and alarms take the whole screen."),
        ],
        "privacy": "Privacy policy",
        "contact": "Contact",
        "rights": "Fakkerni · فكّرني",
        "loading": "Latest",
        "news_h": "What's new in",
        "news_link": "What's new in",
        "all_versions": "All versions and changes",
        "theme": "Switch light or dark",
    },
    "ar": {
        "dir": "rtl",
        "title": "فكّرني · منبّهات وتذكيرات وأدوية لأندرويد",
        "desc": "فكّرني تطبيق مجاني للمنبّهات والتذكيرات والأدوية بالعربية والإنجليزية لأندرويد. بلا حساب ولا إعلانات ولا تتبّع.",
        "nav": ["المزايا", "لقطات الشاشة", "التثبيت", "الخصوصية"],
        "other_lang": "English",
        "download": "تنزيل",
        "eyebrow": "مجاني لأندرويد · قيد الاختبار",
        "h1": "كل ما يهمّك، في موعده",
        "lead": "يرنّ فكّرني بتذكيراتك وجرعات أدويتك في موعدها، حتى دون إنترنت وبعد إعادة تشغيل الهاتف مباشرة. صُمّم بالعربية أولاً مع دعم كامل للإنجليزية.",
        "cta": "نزّل لأندرويد",
        "cta2": "شاهد لقطات الشاشة",
        "meta": "أندرويد ٨ أو أحدث · مجاني · نحو ٦٠ ميغابايت",
        "trust": ["بلا حساب", "بلا إعلانات", "بلا تتبّع", "يعمل دون إنترنت", "عربي وإنجليزي"],
        "features_h": "صُمّم ليرنّ، في كل مرة",
        "features_p": "تذكيرات وأدوية على منبّهات تستمر بالعمل والتطبيق مغلق أو الهاتف في السكون أو بعد إعادة التشغيل.",
        "features": [
            ("bell", "منبّهات ترنّ فعلاً", "منبّه بملء الشاشة فوق شاشة القفل، وفوق التطبيقات الأخرى أثناء استخدامك للهاتف، مع غفوة وتنبيه مسبق وتكرار من كل بضع ساعات إلى كل سنة."),
            ("speak", "اسمع العنوان", "يُنطق التذكير بصوت عالٍ بلغته، عربية أو إنجليزية، مرة واحدة أو كل بضع ثوانٍ."),
            ("pill", "الأدوية ببساطة", "لكل جرعة منبّهها الخاص: أخذتها أو لاحقاً أو تخطّيت. متابعة المخزون وتنبيهات إعادة التعبئة وسجل شهري."),
            ("cloud", "نسخ في Drive الخاص بك", "انسخ إلى مجلد «Fakkerni backups» في Google Drive الخاص بك أو إلى مجلد على هاتفك، مع تشفير اختياري بكلمة مرور."),
            ("power", "موثوق بعد إعادة التشغيل", "ترنّ المنبّهات حتى بعد إعادة تشغيل الهاتف وقبل فتح القفل، وينبّهك فكّرني إن أخّرته أنظمة توفير البطارية."),
            ("globe", "العربية أولاً", "واجهة من اليمين لليسار، وأرقام وجمع عربي صحيح، وأسبوع يبدأ بالسبت، ومظهر فاتح وداكن."),
        ],
        "gallery_h": "نظرة أقرب",
        "gallery_p": "خمس شاشات رئيسية، بالمظهر الفاتح والداكن.",
        "light": "فاتح",
        "dark": "داكن",
        "shots": [("home", "التذكيرات"), ("edit", "تعديل التذكير"), ("medication", "الأدوية"), ("settings", "الإعدادات"), ("backup", "النسخ الاحتياطي")],
        "install_h": "ثبّته في دقيقة",
        "install_p": "فكّرني غير متاح على Google Play بعد. نزّل ملف APK وثبّته مباشرة.",
        "card_h": "فكّرني لأندرويد",
        "card_p": "أحدث إصدار، جاهز للتثبيت.",
        "facts": ["الإصدار", "الحجم", "يتطلّب"],
        "requires": "أندرويد ٨+",
        "checksum": "SHA-256",
        "steps": [
            ("نزّل ملف APK", "اضغط «تنزيل» على هاتفك الأندرويد. اسم الملف fakkerni.apk."),
            ("اسمح بالتثبيت", "افتح الملف. إذا طلب أندرويد ذلك، اسمح بتثبيت التطبيقات من المتصفح أو مدير الملفات."),
            ("افتح فكّرني", "اتبع الإعداد القصير: اللغة والإشعارات وأذونات المنبّه. فعّل «عرض المنبّه فوق التطبيقات» ليظهر المنبّه بملء الشاشة حتى أثناء استخدامك للهاتف. لديك نسخة احتياطية؟ اختر «لديّ نسخة احتياطية، استعادة»."),
        ],
        "note": "قد يحذّرك Google Play Protect من أن التطبيق من مطوّر غير معروف، لأن فكّرني غير متاح على Google Play بعد. اضغط «مزيد من التفاصيل» ثم «التثبيت على أي حال».",
        "privacy_h": "الخصوصية من الأساس",
        "privacy_p": "تذكيراتك وأدويتك شأن شخصي. يحفظها فكّرني على هاتفك، ولا تذهب النسخة الاحتياطية إلا إلى المكان الذي تختاره.",
        "privacy_link": "اقرأ سياسة الخصوصية",
        "checks": [
            "بلا حساب ولا تسجيل",
            "بلا خوادم ولا تحليلات ولا إعلانات",
            "تبقى بياناتك على هاتفك",
            "نسخ اختيارية إلى Google Drive الخاص بك أو مجلد، مشفّرة إن أردت",
        ],
        "faq_h": "أسئلة شائعة",
        "faq": [
            ("هل فكّرني مجاني؟", "نعم. بلا إعلانات ولا اشتراكات ولا مشتريات داخل التطبيق."),
            ("هل يعمل دون إنترنت؟", "نعم. تعمل المنبّهات والتذكيرات والأدوية دون إنترنت بالكامل. يُستخدم الإنترنت فقط عند النسخ إلى Google Drive."),
            ("أين تُحفظ نسخي الاحتياطية؟", "حيث تختار: مجلد «Fakkerni backups» في Google Drive الخاص بك، أو مجلد على هاتفك، أو داخل التطبيق. ويمكنك تشفيرها بكلمة مرور."),
            ("لماذا ليس على Google Play؟", "فكّرني ما زال قيد الاختبار وسيصل إلى Google Play لاحقاً؛ وحتى ذلك الحين يمكنك تثبيت ملف APK من هذه الصفحة."),
            ("ما الهواتف المدعومة؟", "أندرويد ٨ أو أحدث. بعض الشركات تقيّد التطبيقات في الخلفية، ويوضّح إعداد فكّرني كيف تُبقي المنبّهات في موعدها على هاتفك."),
            ("لماذا يظهر المنبّه كإشعار فقط؟", "أثناء استخدامك للهاتف، يعرض أندرويد المنبّهات كإشعار ما لم يُسمح للتطبيق بالظهور فوق التطبيقات الأخرى. فعّل في فكّرني: الإعدادات › الأذونات › «عرض المنبّه فوق التطبيقات»، ليظهر المنبّه بملء الشاشة."),
        ],
        "privacy": "سياسة الخصوصية",
        "contact": "للتواصل",
        "rights": "فكّرني · Fakkerni",
        "loading": "الأحدث",
        "news_h": "الجديد في الإصدار",
        "news_link": "الجديد في الإصدار",
        "all_versions": "كل الإصدارات وتغييراتها",
        "theme": "التبديل بين الفاتح والداكن",
    },
}


def head(t, lang, prefix, title):
    return f"""<!doctype html>
<html lang="{lang}" dir="{t['dir']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="google-site-verification" content="37A9ifyA773BNoFikE5AMEz3uKGSye-tLVznHpkyCa8">
  <title>{title}</title>
  <meta name="description" content="{t['desc']}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{t['desc']}">
  <meta property="og:image" content="https://amrcs92.github.io/fakkerni-site/assets/icon.png">
  <link rel="icon" href="{prefix}assets/icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}style.css">
  <script>try {{ const t = localStorage.getItem('theme'); if (t === 'light' || t === 'dark') document.documentElement.dataset.theme = t; }} catch (e) {{}}
    // Scroll reveals hide content until it is in view, so only when motion is welcome and the browser can tell.
    if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) document.documentElement.classList.add('motion');</script>
</head>
<body>
"""


def topbar(t, lang, prefix, home, other_href, anchors=True):
    logo = (
        f'<a class="brand" href="{home}"><img class="logo-light" src="{prefix}assets/logo-{lang}-light.png" alt="{t["rights"]}">'
        f'<img class="logo-dark" src="{prefix}assets/logo-{lang}-dark.png" alt="{t["rights"]}"></a>'
    )
    ids = ["features", "screenshots", "install", "privacy"]
    links = "".join(f'<a href="{home if not anchors else ""}#{i}">{n}</a>' for i, n in zip(ids, t["nav"]))
    return f"""  <header class="topbar">
    <div class="container">
      {logo}
      <nav class="links" aria-label="Sections">{links}</nav>
      <a class="lang-switch" href="{other_href}" hreflang="{'ar' if lang == 'en' else 'en'}">{t['other_lang']}</a>
      <button type="button" class="theme-toggle" aria-label="{t['theme']}" title="{t['theme']}"><span class="sun">{icon('sun')}</span><span class="moon">{icon('moon')}</span></button>
      <a class="btn btn-primary btn-sm" href="{DOWNLOAD}">{icon('download')}{t['download']}</a>
    </div>
  </header>
"""


def footer(t, lang, prefix, home, privacy):
    return f"""  <footer>
    <div class="container">
      <a href="{home}"><img class="logo-light" src="{prefix}assets/logo-{lang}-light.png" alt="{t['rights']}"><img class="logo-dark" src="{prefix}assets/logo-{lang}-dark.png" alt="{t['rights']}"></a>
      <nav>
        <a href="{privacy}">{t['privacy']}</a>
        <a href="mailto:{CONTACT}">{t['contact']}: {CONTACT}</a>
        <a href="{DOWNLOAD}">{t['download']}</a>
      </nav>
    </div>
  </footer>
  <script>
    // Light / dark switch: starts from the phone's setting, remembers the visitor's choice.
    const isDark = () =>
      document.documentElement.dataset.theme
        ? document.documentElement.dataset.theme === 'dark'
        : matchMedia('(prefers-color-scheme: dark)').matches;
    document.querySelector('.theme-toggle').addEventListener('click', () => {{
      const next = isDark() ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      try {{ localStorage.setItem('theme', next); }} catch (e) {{}}
      document.dispatchEvent(new CustomEvent('themechange', {{ detail: next }}));
    }});
  </script>
"""


def index(lang):
    t = T[lang]
    prefix = "../" if lang == "ar" else ""
    other = "../" if lang == "ar" else "ar/"
    shots = lambda theme: "".join(
        f'<figure data-reveal><div class="phone"><img loading="lazy" src="{prefix}assets/shots/{lang}-{theme}-{k}.png" '
        f'data-light="{prefix}assets/shots/{lang}-light-{k}.png" data-dark="{prefix}assets/shots/{lang}-dark-{k}.png" '
        f'alt="{name}"></div><figcaption>{name}</figcaption></figure>'
        for k, name in t["shots"]
    )
    features = "".join(
        f'<div class="feature" data-reveal><div class="icon">{icon(i)}</div><h3>{h}</h3><p>{p}</p></div>' for i, h, p in t["features"]
    )
    trust = "".join(f"<li>{icon('check')}{x}</li>" for x in t["trust"])
    steps = "".join(f"<li data-reveal><h4>{h}</h4><p>{p}</p></li>" for h, p in t["steps"])
    checks = "".join(f"<li data-reveal>{icon('check')}<span>{x}</span></li>" for x in t["checks"])
    faq = "".join(f"<details data-reveal><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    html = head(t, lang, prefix, t["title"]) + topbar(t, lang, prefix, "./", other) + f"""
  <main>
    <section class="hero">
      <div class="container">
        <div>
          <span class="eyebrow"><span class="dot"></span>{t['eyebrow']}</span>
          <h1>{t['h1']}</h1>
          <p class="lead">{t['lead']}</p>
          <div class="cta">
            <a class="btn btn-primary" href="{DOWNLOAD}">{icon('download')}{t['cta']}</a>
            <a class="btn btn-ghost" href="#screenshots">{t['cta2']}</a>
          </div>
          <p class="meta">{t['meta']}</p>
          <p class="release-line"><a href="#whats-new">{t['news_link']} <span class="rel-v" dir="ltr">{t['loading']}</span></a><span aria-hidden="true">·</span><a href="{RELEASES}">{t['all_versions']}</a></p>
        </div>
        <div class="phones" aria-hidden="true">
          <div class="phone back"><img src="{prefix}assets/shots/{lang}-dark-medication.png" alt=""></div>
          <div class="phone front"><img src="{prefix}assets/shots/{lang}-light-home.png" alt=""></div>
        </div>
      </div>
    </section>

    <div class="trust"><div class="container"><ul>{trust}</ul></div></div>

    <section class="block" id="features">
      <div class="container">
        <div class="section-head" data-reveal><h2>{t['features_h']}</h2><p>{t['features_p']}</p></div>
        <div class="features">{features}</div>
      </div>
    </section>

    <section class="block" id="screenshots" style="background: var(--bg2)">
      <div class="container">
        <div class="section-head" data-reveal><h2>{t['gallery_h']}</h2><p>{t['gallery_p']}</p></div>
        <div class="gallery-bar" data-reveal><div class="seg" role="group">
          <button type="button" data-theme="light" aria-pressed="true">{t['light']}</button>
          <button type="button" data-theme="dark" aria-pressed="false">{t['dark']}</button>
        </div></div>
        <div class="gallery">{shots('light')}</div>
      </div>
    </section>

    <section class="block" id="install">
      <div class="container">
        <div class="section-head" data-reveal><h2>{t['install_h']}</h2><p>{t['install_p']}</p></div>
        <div class="install">
          <div class="download-card" data-reveal>
            <h3>{t['card_h']}</h3>
            <p>{t['card_p']}</p>
            <a class="btn btn-primary" href="{DOWNLOAD}">{icon('download')}{t['cta']}</a>
            <dl class="facts">
              <div><dt>{t['facts'][0]}</dt><dd id="rel-version" dir="ltr">{t['loading']}</dd></div>
              <div><dt>{t['facts'][1]}</dt><dd id="rel-size">~60 MB</dd></div>
              <div><dt>{t['facts'][2]}</dt><dd>{t['requires']}</dd></div>
            </dl>
            <div class="whats-new" id="whats-new" hidden>
              <h4>{t['news_h']} <span class="rel-v" dir="ltr"></span></h4>
              <ul id="rel-news"></ul>
            </div>
            <p class="all-versions"><a href="{RELEASES}">{t['all_versions']}</a></p>
            <p class="checksum" id="rel-sha-wrap" hidden>{t['checksum']}: <code id="rel-sha"></code></p>
          </div>
          <div>
            <ol class="steps">{steps}</ol>
            <p class="note" data-reveal>{t['note']}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="block" id="privacy">
      <div class="container">
        <div class="privacy-band" data-reveal>
          <div>
            <h2>{t['privacy_h']}</h2>
            <p>{t['privacy_p']}</p>
            <a class="btn btn-ghost" href="privacy.html">{t['privacy_link']}</a>
          </div>
          <ul class="checks">{checks}</ul>
        </div>
      </div>
    </section>

    <section class="block" style="padding-top: 0">
      <div class="container">
        <div class="section-head" data-reveal><h2>{t['faq_h']}</h2></div>
        <div class="faq">{faq}</div>
      </div>
    </section>
  </main>
""" + footer(t, lang, prefix, "./", "privacy.html") + f"""
  <script>
    // Screenshot theme switch; it follows the page theme and can be changed on its own.
    const showShots = (theme) => {{
      document.querySelectorAll('.seg button').forEach((x) => x.setAttribute('aria-pressed', String(x.dataset.theme === theme)));
      document.querySelectorAll('.gallery img').forEach((img) => (img.src = img.dataset[theme]));
    }};
    document.querySelectorAll('.seg button').forEach((b) => b.addEventListener('click', () => showShots(b.dataset.theme)));
    if (isDark()) showShots('dark');
    document.addEventListener('themechange', (e) => showShots(e.detail));
    // Latest release facts (version, size, checksum) from GitHub; the page works without them.
    fetch('https://api.github.com/repos/{REPO}/releases/latest')
      .then((r) => (r.ok ? r.json() : null))
      .then((rel) => {{
        if (!rel) return;
        const digits = (s) => {'true' if lang == 'ar' else 'false'} ? s.replace(/\\d/g, (d) => '٠١٢٣٤٥٦٧٨٩'[d]) : s;
        // Version numbers stay in Latin digits: the Arabic zero looks like a dot (٠.١٠.٤).
        const ver = rel.tag_name.replace(/^v/, '');
        document.getElementById('rel-version').textContent = ver;
        document.querySelectorAll('.rel-v').forEach((el) => (el.textContent = ver));
        // What's new: release notes (docs/releases/<tag>.md in the app repo) hold English bullets,
        // then a '### بالعربية' summary, then '---' and the checksum.
        const body = (rel.body || '').split(/\\n---/)[0];
        const parts = body.split(/^###\\s*بالعربية\\s*$/m);
        const plain = (x) => x.replace(/\\*\\*|`/g, '').trim();
        const items = {'true' if lang == 'ar' else 'false'}
          ? (parts[1] || '').split(/\\n+|(?<=\\.)\\s+/).map(plain).filter(Boolean)
          : parts[0].split('\\n').filter((l) => /^\\s*-\\s/.test(l)).map((l) => plain(l.replace(/^\\s*-\\s/, '')));
        if (items.length) {{
          const ul = document.getElementById('rel-news');
          items.slice(0, 4).forEach((x) => {{
            const li = document.createElement('li');
            li.textContent = x;
            ul.appendChild(li);
          }});
          document.getElementById('whats-new').hidden = false;
        }}
        const apk = (rel.assets || []).find((a) => a.name === 'fakkerni.apk');
        if (apk) document.getElementById('rel-size').textContent = digits(String(Math.round(apk.size / 1048576))) + ' MB';
        const m = /SHA-256[^:]*:\\s*`?([a-f0-9]{{64}})/i.exec(rel.body || '');
        if (m) {{
          document.getElementById('rel-sha').textContent = m[1];
          document.getElementById('rel-sha-wrap').hidden = false;
        }}
      }})
      .catch(() => {{}});
  </script>
  <script>
    // Scroll reveal: each item fades up once when it enters the view; items arriving together are staggered.
    if (document.documentElement.classList.contains('motion')) {{
      const io = new IntersectionObserver((entries) => {{
        let n = 0;
        entries.forEach((e) => {{
          if (!e.isIntersecting) return;
          e.target.style.setProperty('--i', Math.min(n++, 5));
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }});
      }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.12 }});
      document.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));
    }}
  </script>
</body>
</html>
"""
    out = os.path.join(ROOT, "ar" if lang == "ar" else "", "index.html")
    open(out, "w", encoding="utf-8", newline="\n").write(html)


def privacy(lang):
    t = T[lang]
    prefix = "../" if lang == "ar" else ""
    other = "../privacy.html" if lang == "ar" else "ar/privacy.html"
    body = open(os.path.join(ROOT, "content", f"privacy.{lang}.html"), encoding="utf-8").read()
    title = ("سياسة الخصوصية · فكّرني" if lang == "ar" else "Privacy policy · Fakkerni")
    html = (
        head(t, lang, prefix, title)
        + topbar(t, lang, prefix, "./", other, anchors=False)
        + f'  <main class="policy">\n{body}\n  </main>\n'
        + footer(t, lang, prefix, "./", "privacy.html")
        + "</body>\n</html>\n"
    )
    out = os.path.join(ROOT, "ar" if lang == "ar" else "", "privacy.html")
    open(out, "w", encoding="utf-8", newline="\n").write(html)


if __name__ == "__main__":
    for language in ("en", "ar"):
        index(language)
        privacy(language)
    print("built")
