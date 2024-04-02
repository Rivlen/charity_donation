document.addEventListener('DOMContentLoaded', function () {
    // Select the "next step" button using its ID
    const nextStepButton = document.getElementById('nextStepBtn1');

    // Listen for clicks on the "next step" button
    nextStepButton.addEventListener('click', function () {
        // Initialize an array to store the values of checked checkboxes
        let selectedCategories = [];

        // Get all checkboxes by their name attribute
        const checkboxes = document.querySelectorAll('input[name="categories"]:checked');

        // Iterate over the checked checkboxes and push their id and name into the array
        checkboxes.forEach(function (checkbox) {
            const categoryData = {
                id: checkbox.value,
                name: checkbox.getAttribute('data-category-name') // Get the category name from data attribute
            };
            selectedCategories.push(categoryData);
        });

        window.localStorage.setItem('selectedCategories', JSON.stringify(selectedCategories));
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Select the "next step" and "previous step" buttons
    const nextStepButton2 = document.getElementById('nextStepBtn2');
    const prevStepButton2 = document.getElementById('prevStepBtn2');

    // Function to save the bags value
    function saveBagsValue() {
        // Select the input by its name attribute
        const bagsInput = document.querySelector('input[name="bags"]');

        // Get the value of the input and convert it to an integer
        const bagsValue = parseInt(bagsInput.value, 10);

        // Store the value in localStorage
        window.localStorage.setItem('bagsValue', bagsValue);
    }

    // Listen for clicks on the "next step" button
    nextStepButton2.addEventListener('click', saveBagsValue);

    // Optionally, if you want to save the value even when going back
    prevStepButton2.addEventListener('click', saveBagsValue);
});


function getInstitutions() { //[1,2,3]
    // Retrieve the selected categories and parse them back into an array of objects
    let selectedCategories = JSON.parse(window.localStorage.getItem('selectedCategories') || '[]');

    // Construct the URL for fetching institutions data
    let myUrl = '/GetInstitutionsByCategoriesAPI?';
    let params = new URLSearchParams();

    selectedCategories.forEach(category => params.append('type_ids', category.id));

    let parameters = params.toString(); // parameters will look like "type_ids=1&type_ids=2&type_ids=3"
    myUrl = myUrl + parameters;

    // Fetch the institutions data
    fetch(myUrl)
        .then(response => response.json())
        .then(data => {

            // Now targeting the newly added container for institutions
            const institutionsContainer = document.getElementById('institutionsContainer');

            // Make sure the container is empty before adding new content
            while (institutionsContainer.firstChild) {
                institutionsContainer.removeChild(institutionsContainer.lastChild);
            }

            // Iterate through each institution and create a radio button for it
            data.forEach(function (institution) {
                const label = document.createElement('label');
                label.classList.add('custom-radio-label');

                const input = document.createElement('input');
                input.type = 'radio';
                input.name = 'organization';
                input.value = institution.id; // Assuming each institution has an 'id' property
                input.setAttribute('data-institution-name', institution.name); // Setting data-institution-name attribute

                const spanCheckbox = document.createElement('span');
                spanCheckbox.classList.add('checkbox', 'radio');

                const spanDescription = document.createElement('span');
                spanDescription.classList.add('description');

                const divTitle = document.createElement('div');
                divTitle.classList.add('title');
                divTitle.textContent = institution.name;

                const divSubtitle = document.createElement('div');
                divSubtitle.classList.add('subtitle');
                divSubtitle.textContent = 'Cel i misja: ' + institution.description;

                // Assemble the elements
                spanDescription.appendChild(divTitle);
                spanDescription.appendChild(divSubtitle);

                label.appendChild(input);
                label.appendChild(spanCheckbox);
                label.appendChild(spanDescription);

                // Append the newly created label to the institutions container
                institutionsContainer.appendChild(label);
            });
        });

}


document.getElementById('nextStepBtn3').addEventListener('click', function () {
    // Get all radio buttons with the name 'organization'
    const radios = document.querySelectorAll('input[name="organization"]');

    // Find the checked radio button
    const selectedRadio = Array.from(radios).find(radio => radio.checked);

    // If an institution is selected
    if (selectedRadio) {
        // Assuming the institution's name is stored in a data attribute or is the text content of a sibling element
        // For example, using a data attribute like 'data-institution-name'
        const institutionName = selectedRadio.getAttribute('data-institution-name');

        // If the institution's name isn't stored in a data attribute, and you have a structure like:
        // <label><input type="radio" name="organization" value="ID">Institution Name</label>
        // You might use `selectedRadio.nextSibling.textContent.trim()` or a similar approach depending on your HTML structure

        // Store the selected institution as an object with both ID and name
        const selectedInstitution = {
            id: selectedRadio.value,
            name: institutionName // Replace this line with the correct way to obtain the name based on your HTML
        };

        window.localStorage.setItem('selectedInstitution', JSON.stringify(selectedInstitution));

        console.log("Selected institution stored:", JSON.stringify(selectedInstitution));
    } else {
        // Handle the case where no institution is selected (if necessary)
        console.log("No institution selected.");
    }
});


document.getElementById('nextStepBtn4').addEventListener('click', function () {
    // Object to hold the data from step 4
    const pickupDetails = {
        address: document.querySelector('input[name="address"]').value,
        city: document.querySelector('input[name="city"]').value,
        postcode: document.querySelector('input[name="postcode"]').value,
        phone: document.querySelector('input[name="phone"]').value,
        date: document.querySelector('input[name="date"]').value,
        time: document.querySelector('input[name="time"]').value,
        more_info: document.querySelector('textarea[name="more_info"]').value
    };

    // Store the pickup details in localStorage
    window.localStorage.setItem('pickupDetails', JSON.stringify(pickupDetails));

    console.log("Pickup details stored:", pickupDetails);
});

function displaySummary() {
    // Retrieve data from localStorage
    const selectedCategories = JSON.parse(window.localStorage.getItem('selectedCategories')) || [];
    const selectedInstitutionObject = JSON.parse(window.localStorage.getItem('selectedInstitution')); // Now an object, not just the ID
    const bagsValue = JSON.parse(window.localStorage.getItem('bagsValue'))
    const pickupDetails = JSON.parse(window.localStorage.getItem('pickupDetails')) || {};

    // Use the names directly from the selectedCategories objects
    const categoriesSummaryText = selectedCategories.map(category => category.name).join(', ');
    const institutionName = selectedInstitutionObject ? `Instytucja "${selectedInstitutionObject.name}"` : "Nie wybrano instytucji"; // Using the name from the selectedInstitution object

    // Construct HTML content for donation summary
    let donationSummaryHtml = `
        <li>
            <span class="icon icon-bag"></span>
            <span class="summary--text">${bagsValue} worków z kategorii: ${categoriesSummaryText}</span>
        </li>
        <li>
            <span class="icon icon-hand"></span>
            <span class="summary--text">${institutionName}</span>
        </li>`;

    // Construct HTML content for address details
    let addressDetailsHtml = `
        <li>${pickupDetails.address}</li>
        <li>${pickupDetails.city}</li>
        <li>${pickupDetails.postcode}</li>
        <li>${pickupDetails.phone}</li>`;

    // Construct HTML content for pickup details
    let pickupDetailsHtml = `
        <li>${pickupDetails.date}</li>
        <li>${pickupDetails.time}</li>
        <li>${pickupDetails.more_info || 'Brak uwag'}</li>`;

    // Update the DOM elements with the constructed HTML content
    document.querySelector('#step5 .form-section:nth-child(1) ul').innerHTML = donationSummaryHtml;
    document.querySelector('#step5 .form-section--columns .form-section--column:nth-child(1) ul').innerHTML = addressDetailsHtml;
    document.querySelector('#step5 .form-section--columns .form-section--column:nth-child(2) ul').innerHTML = pickupDetailsHtml;
}


// Call displaySummary when step 5 is about to be shown
document.getElementById('nextStepBtn4').addEventListener('click', displaySummary);


document.addEventListener('DOMContentLoaded', function () {
    const nextBtns = document.querySelectorAll('.next-step');
    const prevBtns = document.querySelectorAll('.prev-step');
    const steps = document.querySelectorAll('div[data-step]');
    let currentStep = 1;

    function showStep(step) {
        steps.forEach((div) => {
            div.style.display = 'none';
            if (parseInt(div.getAttribute('data-step')) === step) {
                div.style.display = 'block';
            }
        });
        document.querySelector('.form--steps-counter span').textContent = step.toString();
    }

    nextBtns.forEach((btn) => {
        btn.addEventListener('click', () => {
            if (currentStep === 2) {
                getInstitutions();
            }
            if (currentStep < steps.length) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });

    prevBtns.forEach((btn) => {
        btn.addEventListener('click', () => {
            if (currentStep > 1) {
                currentStep--;
                showStep(currentStep);
            }
        });
    });

    showStep(currentStep);

    document.getElementById("category-choice").innerHTML = "{{serialized_categories}}";
});

