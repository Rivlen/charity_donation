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
                filterInstitutions();
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

    let chosen_categories = null
    document.getElementById("category-choice").innerHTML = "{{serialized_categories}}";
});


// <div className="form-group form-group--checkbox">
//     <label>
//         <input type="checkbox" name="categories" value={{category.id}}/>
//         <span className="checkbox"></span>
//         <span className="description">{{category.name}}</span>
//     </label>
// </div>