document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("packageForm");
    if (!form) return;

    form.addEventListener("submit", function (event) {
        const fields = form.querySelectorAll("input");
        let hasEmptyField = false;

        fields.forEach(function (field) {
            if (field.type !== "hidden" && field.value.trim() === "") {
                hasEmptyField = true;
                field.classList.add("invalid");
            } else {
                field.classList.remove("invalid");
            }
        });

        const error = document.getElementById("clientError");
        if (hasEmptyField) {
            event.preventDefault();
            error.textContent = "Please fill in all fields before submitting.";
        } else {
            error.textContent = "";
        }
    });
});
