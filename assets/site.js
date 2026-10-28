const toggle = document.querySelector(".menu-toggle");
const nav = document.getElementById("nav");

toggle.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});

nav.addEventListener("click", (e) => {
  if (e.target.matches("a")) nav.classList.remove("open");
});

const fades = document.querySelectorAll(".fade-in");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.replace("pending", "shown");
        io.unobserve(e.target);
      }
    });
  });
  fades.forEach((el) => {
    el.classList.add("pending");
    io.observe(el);
  });
}

const contactForm = document.querySelector(".contact-form");
if (contactForm) {
  const status = contactForm.querySelector(".form-status");
  const button = contactForm.querySelector("button[type=submit]");

  contactForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(contactForm));
    data._subject = `Website contact: ${data.subject}`;
    data._replyto = data.email;

    button.disabled = true;
    status.textContent = "Sending…";
    try {
      const res = await fetch(contactForm.action.replace("formsubmit.co/", "formsubmit.co/ajax/"), {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(data),
      });
      const json = await res.json();
      if (!res.ok || json.success === "false" || json.success === false) throw new Error(json.message);
      contactForm.reset();
      status.textContent = "Thanks! Your message has been sent.";
    } catch {
      status.textContent = "Sorry, something went wrong. Please try again later.";
    } finally {
      button.disabled = false;
    }
  });
}
