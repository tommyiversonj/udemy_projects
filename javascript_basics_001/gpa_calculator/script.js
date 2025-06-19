// script.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("gpa-form");
    const resultsDiv = document.getElementById("results");

    document.getElementById("add-course").addEventListener("click", () => {
        const newCourse = document.querySelector(".course-entry").cloneNode(true);
        newCourse.querySelectorAll("input, select").forEach(input => {
            input.value = "";
        });
        form.insertBefore(newCourse, form.children[form.children.length - 2]);
    });

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        let totalCredits = 0;
        let totalPoints = 0;
        let courseList = "";

        const entries = form.querySelectorAll(".course-entry");
        entries.forEach(entry => {
            const courseName = entry.children[0].value.trim();
            const credit = parseFloat(entry.children[1].value);
            const grade = parseFloat(entry.children[2].value);

            if (!isNaN(credit) && !isNaN(grade)) {
                totalCredits += credit;
                totalPoints += grade * credit;
                courseList += `<p>${courseName} (${credit} credits): Grade ${grade}</p>`;
            }
        });

        if (totalCredits === 0) {
            resultsDiv.innerHTML = "<p>Please enter valid courses and credit hours.</p>";
            return;
        }

        const gpa = (totalPoints / totalCredits).toFixed(2);
        resultsDiv.innerHTML = `
      <h3>Results</h3>
      ${courseList}
      <p><strong>Total Credits:</strong> ${totalCredits}</p>
      <p><strong>GPA:</strong> ${gpa}</p>
    `;
    });
});
