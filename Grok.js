console.log("Gork.js loaded");

// Navbar Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
if (hamburger && navMenu) {
  hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
  });
}

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const targetSelector = this.getAttribute('href');
    const targetElement = document.querySelector(targetSelector);
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Impact Counter
const counters = document.querySelectorAll('.counter');
counters.forEach(counter => {
  let hasCounted = false;
  const updateCounter = () => {
    const target = +counter.getAttribute('data-target');
    let count = +counter.innerText;
    const speed = 200;
    const increment = target / speed;
    if (count < target) {
      counter.innerText = Math.ceil(count + increment);
      setTimeout(updateCounter, 10);
    } else {
      counter.innerText = target;
    }
  };
  const onScroll = () => {
    const rect = counter.getBoundingClientRect();
    if (!hasCounted && rect.top < window.innerHeight) {
      updateCounter();
      hasCounted = true;
      window.removeEventListener('scroll', onScroll);
    }
  };
  window.addEventListener('scroll', onScroll);
  onScroll();
});

// Testimonial Carousel
const carouselItems = document.querySelectorAll('.carousel-item');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let currentIndex = 0;
function showSlide(index) {
  carouselItems.forEach(item => item.classList.remove('active'));
  if (carouselItems[index]) {
    carouselItems[index].classList.add('active');
  }
}
if (prevBtn && nextBtn && carouselItems.length) {
  prevBtn.addEventListener('click', () => {
    currentIndex = currentIndex === 0 ? carouselItems.length - 1 : currentIndex - 1;
    showSlide(currentIndex);
  });
  nextBtn.addEventListener('click', () => {
    currentIndex = currentIndex === carouselItems.length - 1 ? 0 : currentIndex + 1;
    showSlide(currentIndex);
  });
  setInterval(() => {
    currentIndex = currentIndex === carouselItems.length - 1 ? 0 : currentIndex + 1;
    showSlide(currentIndex);
  }, 5000);
}

// Contact Form Submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  console.log("Contact form found");
  contactForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent page reload
    console.log("Form submitted");
    const formData = new FormData(this);

    fetch('submit_contact.php', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        alert('Thank you! Your message has been submitted successfully.');
        this.reset();
      } else {
        alert('Error: ' + data.message);
      }
    })
    .catch(error => {
      console.error('Fetch error:', error);
      alert('Something went wrong. Please try again.');
    });
  });
}