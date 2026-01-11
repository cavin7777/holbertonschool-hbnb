// ------------------- UTILITY FUNCTIONS -------------------

// Get a cookie value by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// Delete a cookie by name
function deleteCookie(name) {
    document.cookie = `${name}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC;`;
}

// Extract place ID from URL
function getPlaceIdFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('id');
}

// ------------------- AUTHENTICATION -------------------

// Check authentication for index/place pages
function checkAuthentication(showUI = true) {
    const token = getCookie('token');

    if (showUI) {
        // Login/logout links in header
        const loginLink = document.getElementById('login-link');
        const logoutLink = document.getElementById('logout-link');
        if (loginLink) loginLink.style.display = token ? 'none' : 'block';
        if (logoutLink) logoutLink.style.display = token ? 'block' : 'none';

        // Place page review form
        const addReviewSection = document.getElementById('add-review');
        if (addReviewSection) addReviewSection.style.display = token ? 'block' : 'none';
    }

    return token;
}

// Logout button setup
function setupLogout() {
    const logoutLink = document.getElementById('logout-link');
    if (!logoutLink) return;

    logoutLink.addEventListener('click', () => {
        deleteCookie('token');
        window.location.reload();
    });
}

// ------------------- LOGIN HANDLER -------------------

async function handleLogin(event) {
    event.preventDefault();

    const email = document.getElementById('email')?.value.trim();
    const password = document.getElementById('password')?.value.trim();

    if (!email || !password) {
        alert('Please enter both email and password.');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (!response.ok) {
            alert('Login failed: ' + (data.message || response.statusText));
            return;
        }

        if (!data.access_token) {
            alert('Login failed: No token returned by server.');
            return;
        }

        // Store token in cookie for 1 day
        const expiry = new Date();
        expiry.setTime(expiry.getTime() + 24 * 60 * 60 * 1000);
        document.cookie = `token=${data.access_token}; path=/; expires=${expiry.toUTCString()};`;

        alert(`Login successful! Welcome, ${email}`);
        window.location.href = 'index.html'; // redirect after login

    } catch (error) {
        console.error('Error during login:', error);
        alert('Login failed: Network or server error.');
    }
}

// ------------------- FETCH & DISPLAY PLACES (INDEX) -------------------

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': token ? `Bearer ${token}` : undefined
            }
        });

        if (!response.ok) throw new Error('Failed to fetch places');

        const places = await response.json();
        window.allPlaces = places;
        displayPlaces(places);

    } catch (error) {
        console.error('Error fetching places:', error);
        alert('Could not load places. Check console for details.');
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = '';
    places.forEach(place => {
        const div = document.createElement('div');
        div.className = 'place-card';
        div.dataset.price = place.price;
        div.innerHTML = `
            <h3>${place.title}</h3>
            <p>Price per night: $${place.price}</p>
            <p>${place.description || ''}</p>
            <button onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
        `;
        placesList.appendChild(div);
    });
}

// ------------------- PRICE FILTER (INDEX) -------------------

function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    if (!priceFilter) return;

    priceFilter.addEventListener('change', (event) => {
        const maxPrice = event.target.value;
        const places = document.querySelectorAll('.place-card');

        places.forEach(place => {
            const price = parseFloat(place.dataset.price);
            place.style.display = maxPrice === 'All' || price <= parseFloat(maxPrice) ? 'block' : 'none';
        });
    });
}

// ------------------- FETCH & DISPLAY PLACE DETAILS (PLACE.HTML) -------------------

async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': token ? `Bearer ${token}` : undefined
            }
        });

        if (!response.ok) throw new Error('Failed to fetch place details');

        const place = await response.json();
        displayPlaceDetails(place);

    } catch (error) {
        console.error('Error fetching place details:', error);
        alert('Could not load place details. Check console for details.');
    }
}

function displayPlaceDetails(place) {
    const placeInfo = document.getElementById('place-info');
    if (!placeInfo) return;

    placeInfo.innerHTML = `
        <h2>${place.title}</h2>
        <p>Host: ${place.user?.email || "Unknown"}</p>
        <p>Price per night: $${place.price}</p>
        <p>Description: ${place.description || ""}</p>
        <p>Amenities: ${place.amenities?.map(a => a.name).join(", ") || "None"}</p>
    `;

    displayReviews(place.reviews || []);
}

// ------------------- REVIEWS -------------------

function displayReviews(reviews) {
    const reviewsSection = document.getElementById('reviews');
    if (!reviewsSection) return;

    reviewsSection.innerHTML = '';
    reviews.forEach(r => {
        const div = document.createElement('div');
        div.className = 'review-card';
        div.innerHTML = `<p>"${r.text}"</p><p>By ${r.user?.email || "Unknown"}, Rating: ${r.rating}</p>`;
        reviewsSection.appendChild(div);
    });
}

// ------------------- REVIEW FORM -------------------

async function submitReview(token, placeId, reviewText, rating) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ text: reviewText, rating: rating })
        });

        if (response.ok) {
            alert('Review submitted successfully!');
            const form = document.getElementById('review-form');
            if (form) form.reset();
            window.location.href = `place.html?id=${placeId}`;
        } else {
            const errorData = await response.json();
            alert('Failed to submit review: ' + (errorData.message || response.statusText));
        }
    } catch (error) {
        console.error('Error submitting review:', error);
        alert('Network or server error. Could not submit review.');
    }
}

function handleReviewForm(token) {
    const reviewForm = document.getElementById('review-form');
    if (!reviewForm) return;

    reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const placeId = getPlaceIdFromURL();
        const reviewText = document.getElementById('review-text').value.trim();
        const rating = parseInt(document.getElementById('rating').value);

        if (!reviewText || !rating || rating < 1 || rating > 5) {
            alert('Please provide a valid review and rating (1-5).');
            return;
        }

        await submitReview(token, placeId, reviewText, rating);
    });
}

// ------------------- PAGE LOAD -------------------

document.addEventListener('DOMContentLoaded', () => {
    const token = checkAuthentication();
    setupLogout();

    // Attach login form handler globally
    const loginForm = document.getElementById('login-form');
    if (loginForm) loginForm.addEventListener('submit', handleLogin);

    // INDEX PAGE
    const placesList = document.getElementById('places-list');
    if (placesList) {
        fetchPlaces(token);
        setupPriceFilter();
    }

    // PLACE PAGE
    const placeInfo = document.getElementById('place-info');
    if (placeInfo) {
        const placeId = getPlaceIdFromURL();
        if (placeId) fetchPlaceDetails(token, placeId);
        if (token) handleReviewForm(token);
    }

    // REVIEW FORM PAGE (add-review)
    const reviewForm = document.getElementById('review-form');
    if (reviewForm && !token) {
        alert('You must be logged in to add a review.');
        window.location.href = 'index.html';
    }
});
