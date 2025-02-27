// Navbar Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger && navMenu) { // Check that elements exist
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
    if (targetElement) { // Check if the target exists
      targetElement.scrollIntoView({
        behavior: 'smooth'
      });
    }
  });
});

// Impact Counter
const counters = document.querySelectorAll('.counter');
counters.forEach(counter => {
  let hasCounted = false; // Flag to avoid multiple counts

  const updateCounter = () => {
    const target = +counter.getAttribute('data-target');
    let count = +counter.innerText;
    const speed = 200; // Adjust this value for speed
    const increment = target / speed;

    if (count < target) {
      counter.innerText = Math.ceil(count + increment);
      setTimeout(updateCounter, 10);
    } else {
      counter.innerText = target;
    }
  };

  // Check once on scroll and remove listener after counting
  const onScroll = () => {
    const rect = counter.getBoundingClientRect();
    if (!hasCounted && rect.top < window.innerHeight) {
      updateCounter();
      hasCounted = true;
      window.removeEventListener('scroll', onScroll);
    }
  };

  window.addEventListener('scroll', onScroll);
  // Also check if counter is in view on page load
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

// Check if buttons exist before adding event listeners
if (prevBtn && nextBtn && carouselItems.length) {
  prevBtn.addEventListener('click', () => {
    currentIndex = currentIndex === 0 ? carouselItems.length - 1 : currentIndex - 1;
    showSlide(currentIndex);
  });

  nextBtn.addEventListener('click', () => {
    currentIndex = currentIndex === carouselItems.length - 1 ? 0 : currentIndex + 1;
    showSlide(currentIndex);
  });

  // Auto-rotate slides every 5 seconds
  setInterval(() => {
    currentIndex = currentIndex === carouselItems.length - 1 ? 0 : currentIndex + 1;
    showSlide(currentIndex);
  }, 5000);
}
