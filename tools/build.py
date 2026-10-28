"""Builds the site's HTML pages. Run from anywhere: python3 tools/build.py

Shared header, footer and page content live here; story text lives in
tools/content/<slug>.html (one <p> per paragraph). Edit those, rebuild,
then commit the generated .html files.
"""
import pathlib
R=pathlib.Path(__file__).resolve().parent.parent
CONTENT=R/'tools'/'content'
AMAZON='https://www.amazon.co.uk/Odinsbane-Waters-Mimir-Saga/dp/B0DX1754L5'
CONTACT_EMAIL='nikolai.sie@gmail.com'

STORIES='''<li class="has-sub"><a href="#" aria-haspopup="true">Free Stories<i class="fas fa-caret-down" aria-hidden="true"></i></a>
          <ul>
            <li><a href="/free-stories/jotunheist/">Jotunheist</a></li>
            <li><a href="/free-stories/witchblade/">Witchblade</a></li>
          </ul>
        </li>'''

def head(title,depth,desc=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc or 'Nikolai Sie writes Norse fantasy. Odinsbane is out now.'}">
<link rel="icon" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link rel="stylesheet" href="/assets/style.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">Nikolai Sie</a>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
    <nav id="nav" class="nav">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/#bio">About</a></li>
        <li><a href="/odinsbane/">Odinsbane</a></li>
        {STORIES}
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="content">
'''

TAIL=f'''</main>
<section class="subscribe">
  <div class="wrap">
    <h2 class="fade-in">Subscribe to my mailing list</h2>
    <form class="sub-form" method="post" action="#" name="subscribe">
      <input type="email" name="email" placeholder="Email" required aria-label="Email">
      <button type="submit">Subscribe</button>
    </form>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap footer-inner">
    <p>&copy; 2024, Nikolai Sie</p>
    <nav class="footer-nav">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/#bio">About</a></li>
        <li><a href="/odinsbane/">Odinsbane</a></li>
        {STORIES}
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </nav>
  </div>
</footer>
</body>
</html>
'''

blurb='''<p>All who live in the Viking world worship Odin, but my sister Ronja and I grew up in the ruins of his mistakes. Desperate to stop the end of the world, he destroyed our home as a sacrifice to his enemies. We have sworn to teach him that his arrogance has consequences—even for the king of the gods.</p>
<p>After years of hunting him, we finally have a trail. A mysterious witch offers us the knowledge of her coven and a chance to redeem the last remnant of our past. When we follow her, we open the door to a world of lore and witchcraft, where great powers battle each other with brutal might and ruthless deceit.</p>
<p>Ronja and I are strangers here. We have to make this world our own.</p>'''

def book(title,btn):
    return f'''<section class="hero">
  <div class="wrap">
    <h2 class="hero-title">{title}</h2>
  </div>
  <div class="wrap book">
    <div class="book-text">
      {blurb}
      {btn}
    </div>
    <div class="book-cover"><img src="/assets/img/odinsbane-cover.png" alt="Odinsbane cover" width="913" height="1106"></div>
  </div>
'''

def write(path,content):
    f=R/path; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(content)

# Home
home=head('Nikolai Sie',0)+book('Odinsbane is out now',f'<a class="btn" href="{AMAZON}" target="_blank" rel="noopener">Buy on Amazon<i class="fab fa-amazon" aria-hidden="true"></i></a>')+'''  <div class="wrap about" id="bio">
    <div class="about-img"><img src="/assets/img/nikolai-sie.jpeg" alt="Nikolai Sie" width="768" height="1024"></div>
    <div class="about-text">
      <h2>About the Author</h2>
      <p>Nikolai is a Norwegian living far from home and writing Norse Fantasy to remember that he comes from a place that blooms in the spring and freezes in the winter.</p>
    </div>
  </div>
</section>
'''+TAIL
write('index.html',home)

# Odinsbane
write('odinsbane/index.html',head('Odinsbane - Nikolai Sie',1)+book('Odinsbane is coming soon','<a class="btn" href="#link">Buy on Amazon<i class="fab fa-amazon" aria-hidden="true"></i></a>')+'</section>\n'+TAIL)

# Contact
def field(id_,label,type_='text'):
    return f'<div class="field"><label for="{id_}">{label}</label><input id="{id_}" name="{id_}" type="{type_}" required></div>'
write('contact/index.html',head('Contact - Nikolai Sie',1)+f'''<section class="hero hero-short">
  <div class="wrap contact">
    <h2 class="page-title center">Get in touch</h2>
    <form class="contact-form" method="post" action="https://formsubmit.co/{CONTACT_EMAIL}" name="contact">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="two">{field('first-name','First Name')}{field('last-name','Last Name')}</div>
      {field('email','Email','email')}
      {field('subject','Subject')}
      <div class="field"><label for="message">Message</label><textarea id="message" name="message" rows="5" required></textarea></div>
      <button class="form-btn" type="submit">Submit</button>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
'''+TAIL)

# Stories
for slug,title in [('jotunheist','Jotunheist'),('witchblade','Witchblade')]:
    paras=(CONTENT/f'{slug}.html').read_text().strip()
    write(f'free-stories/{slug}/index.html',head(f'{title} - Nikolai Sie',2)+f'''<section class="hero hero-short">
  <div class="wrap story">
    <h2 class="page-title">{title}</h2>
    {paras}
  </div>
</section>
'''+TAIL)

# 404
write('404.html',head('Page not found - Nikolai Sie',0)+'''<section class="hero hero-short">
  <div class="wrap contact not-found">
    <h2 class="page-title center">Page not found</h2>
    <p>The page you were looking for doesn&rsquo;t exist or has moved.</p>
    <a class="btn" href="/">Back to home</a>
  </div>
</section>
'''+TAIL)
