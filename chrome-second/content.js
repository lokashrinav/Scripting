function waitForPageLoad() {
  return new Promise(resolve => {
    if (document.readyState === "complete") {
      resolve();
    } else {
      window.addEventListener('load', resolve);
    }
  });
}

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {

  async function handleFileUpload() {
    const fileLink = "https://raw.githubusercontent.com/lokashrinav/Jake_Resume/main/Jake_Resume.pdf"; 
    let response = await fetch(fileLink);    
    response = await response.blob()
    let file = new File([response], "Jake_Resume.pdf");
    let input = document.querySelector('input[type="file"]');
    let container = new DataTransfer();
    container.items.add(file)
    input.files = container.files

    const event = new Event("change", {
      bubbles: !0,
    });
    input.dispatchEvent(event);

  }

  function dispatchChangeEvent(element) {
    const event = new Event('change', { bubbles: true });
    element.dispatchEvent(event);
  }


  async function next() {
    let button = document.querySelector('.css-1nnif6c');
    if (button) {
      button.click();  // Assuming this changes page/content
    }
  
  }

  function typeText(element, text) {
    for (let char of text) {
      element.dispatchEvent(new KeyboardEvent('keydown', { key: char }));
      element.dispatchEvent(new KeyboardEvent('keypress', { key: char }));
      element.value += char; // Update the value manually
      element.dispatchEvent(new KeyboardEvent('input', { key: char }));
      element.dispatchEvent(new KeyboardEvent('keyup', { key: char }));
    }
  }

  async function experience() {
    let jobNames = ["Trading and Technology Program Participant", "Software Engineer Intern", "Software Quality Assurance Intern", "Coding Instructor"];
    let startMonths = ["03", "06", "06", "09"];
    let endMonths = ["03", "08", "08", "Present"];
    let startYears = ["2024", "2023", "2022", "2022"];
    let endYears = ["2024", "2023", "2022", ""];
    let companyNames = ["Jane Street", "iQuasar", "Skill Struck", "Computer CORE"];
    let jobDescriptions = [
        "Analyzed market trends, built a program to trade effectively on a simulated market, engaged in multiple problem-solving and trading games, learnt about trading, software engineering, and financial markets",
        "Utilized HTML, CSS, and JavaScript to design and develop a user-friendly interface for a new software product, incorporating responsive design principles, navigation menus, and interactive elements to enhance usability. Integrated Java functionalities into the frontend design, optimizing software performance and reducing loading times by 50%, incorporating backend features into the frontend, resulting in high performance. Implemented automated software testing using Selenium to identify and address bugs, with 10+ tickets issued, leading to a 30% decrease in post-launch issue reports.",
        "Conducted manual and automated testing of web applications, resulting in a 20% decrease in post-release defects. Developed comprehensive test cases and test scripts, leading to a 30% improvement in test coverage. Contributed insights for process improvements, leading to a 10% increase in overall QA efficiency. Utilized testing tools such as Selenium, saving approximately 15 hours per week in manual testing efforts.",
        "Taught coding to 50+ students with no coding experience by achieving an average score of 85% in assessments on a Python coding curriculum, which covered essential programming concepts, such as variables, data types, functions, if-else statements, loops, and file input/output using lessons and projects"
    ];
    let currentWork = ["False", "False", "False", "True"];    
  
    for(let i = 0; i < companyNames.length; i++) {
      let x = document.querySelector(`div[data-automation-id="workExperience-${i + 1}"]`)
      let button;
      if(!x) {
        if(i == 0) {
          button = document.querySelector('button[data-automation-id="Add"]')
        }
        else{
          button = document.querySelector('button[data-automation-id="Add Another"]')
        }
        if (button) {
          button.click()
          await new Promise(resolve => setTimeout(resolve, 1000));
        }
      }
      let jobInput = document.querySelectorAll(`input[data-automation-id="jobTitle"]`)[i]
      let companyNameInput = document.querySelectorAll(`input[data-automation-id="company"]`)[i]
      let jobDescriptionInput = document.querySelectorAll(`textarea[data-automation-id="description"]`)[i]    
      let monthInput = document.querySelectorAll(`input[data-automation-id="dateSectionMonth-input"]`)[2 * i]    
      let monthInput2 = document.querySelectorAll(`input[data-automation-id="dateSectionMonth-input"]`)[(2 * i) + 1]    
      let yearInput = document.querySelectorAll(`input[data-automation-id="dateSectionYear-input"]`)[2 * i]    
      let yearInput2 = document.querySelectorAll(`input[data-automation-id="dateSectionYear-input"]`)[(2 * i) + 1]    
      if (jobInput) {
        companyNameInput.value = jobNames[i];
        jobInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
      if (companyNameInput) {
          companyNameInput.value = companyNames[i];
          companyNameInput.dispatchEvent(new Event('change', { bubbles: true }));
      }
    if (jobDescriptionInput) {
        jobDescriptionInput.value = jobDescriptions[i];
        jobDescriptionInput.dispatchEvent(new Event('input', { bubbles: true }));
    }
    if (monthInput) {
        monthInput.value = startMonths[i];
        monthInput.dispatchEvent(new Event('input', { bubbles: true }));
        monthInput.focus(); // Focus on the input element
        monthInput.click(); // Simulate click event
        monthInput.click(); // Simulate click event
    }
    if (monthInput2) {
        monthInput2.value = endMonths[i];
        monthInput2.dispatchEvent(new Event('input', { bubbles: true }));
        monthInput2.focus(); // Focus on the input element
        monthInput2.click(); // Simulate click event
        monthInput2.click(); // Simulate click event
    }
    if (yearInput) {
        yearInput.value = startYears[i];
        yearInput.dispatchEvent(new Event('input', { bubbles: true }));
        yearInput.focus(); // Focus on the input element
        yearInput.click(); // Simulate click event
        yearInput.click(); // Simulate click event
    }
    if (yearInput2) {
        yearInput2.value = endYears[i];
        yearInput2.dispatchEvent(new Event('input', { bubbles: true }));
        yearInput2.focus(); // Focus on the input element
        yearInput2.click(); // Simulate click event
        yearInput2.click(); // Simulate click event
    }    
    }
  }  

  async function school() {
    if (!document.querySelector(`div[data-automation-id="education-1"]`)) {
      let button = document.querySelector(`button[aria-label="Add Education"]`)
      button.click()
      await new Promise(resolve => setTimeout(resolve, 2000));
    }
    let head = document.querySelector(`div[data-automation-id="education-1"]`)
    startYear = ["2023"]
    endYear = ["2026"]
    schoolNames = ["University of Maryland - College Park"]
    
    let startYearInput2 = head.querySelectorAll(`input[data-automation-id="dateSectionYear-input"]`)[0]
    if (startYearInput2) {
      startYearInput2.value = startYear[0]
      startYearInput2.dispatchEvent(new Event('input', { bubbles: true }));
      startYearInput2.focus(); // Focus on the input element
      startYearInput2.click(); // Simulate click event
    }
    
    let schoolNameInput = document.querySelectorAll(`input[data-automation-id="school"]`)[0]
    if (schoolNameInput) {
      schoolNameInput.value = schoolNames[0]
      schoolNameInput.dispatchEvent(new Event('input', { bubbles: true }))
      schoolNameInput.focus(); // Focus on the input element
      schoolNameInput.click(); // Simulate click event;
    }
    
    let endYearInput = head.querySelectorAll(`input[data-automation-id="dateSectionYear-input"]`)[1]
    if (endYearInput) {
      endYearInput.value = endYear[0]
      endYearInput.dispatchEvent(new Event('input', { bubbles: true }));
      endYearInput.focus(); // Focus on the input element
      endYearInput.click(); // Simulate click event
    }
    
    let degreeButton = document.querySelectorAll(`button[data-automation-id="degree"]`)[0]
    if (degreeButton) {
      degreeButton.click()
      await new Promise(resolve => setTimeout(resolve, 1000));
      let divElements = document.querySelectorAll('div');
      divElements.forEach(div => {
        if (div.textContent.includes("Bachelors")) {
          div.parentNode.click()
        }
      });      
    }
  }
  
  async function websites() {

  }

  async function sklls() {
    
  }

  async function page2() {
    let button1 = document.querySelector('input[id="2"]');
    button1.click()
    let firstNameInput = document.querySelector('input[data-automation-id]="legalNameSection_firstName"')
    firstNameInput.value = "Jake"
    let lastNameInput = document.querySelector('input[data-automation-id]="legalNameSection_lastName"')
    lastNameInput.value = "Ryan"
    let addressInput = document.querySelector('input[data-automation-id]="addressSection_addressLine1"')
    addressInput.value = "123 Pine Cone St"
    let cityInput = document.querySelector('input[data-automation-id]="addressSection_city"')
    cityInput.value = "Love City"
    let postalInput = document.querySelector('input[data-automation-id]="addressSection_postalCode"')
    postalInput.value = "12345"
    let phoneNumberInput = document.querySelector('input[data-automation-id]="phone-number"')
    phoneNumberInput.value = "571-525-6131"


    // Get the dropdown button element by its ID
    var dropdownButton = document.getElementById("input-17");

    // Simulate a click event on the dropdown button to trigger the dropdown
    dropdownButton.click();

    // Get the dropdown options
    var dropdownOptions = document.querySelectorAll("[role='option']");

    // Select the first option
    if (dropdownOptions.length > 0) {
        dropdownOptions[0].click();
    }
    let secondDropDown = document.querySelectorAll('span[class="css-10xelx9"]')[1];
    secondDropDown.click()
    document.getElementById('m54r5v').checked = true;
  }

  async function schoolNext() {
    let button = document.querySelector('button[data-automation-id="bottom-navigation-next-button"]')
    button.click()

  }

  async function main() {
    /*await handleFileUpload();
    await next();
    setTimeout(() => { next(); }, 5000);*/
    await experience();
    await school();
    await schoolNext()
  }

  main()
});



