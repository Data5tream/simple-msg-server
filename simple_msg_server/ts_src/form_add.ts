const typeOptions = [
    'text',
    'email',
];

const fieldList = document.getElementById('fieldList') as HTMLDivElement;
let fieldCount = 0;

/**
 * Add a new form field to the form
 */
const addField = () => {
    // create row container
    const rowElement = document.createElement('div');
    rowElement.className = 'mb-3 row field';

    // create label element
    const label = document.createElement('label');
    label.className = 'visually-hidden';
    label.innerText = 'Name';
    label.setAttribute('for', `field${fieldCount}`);

    // append label to row
    rowElement.appendChild(label);

    // create name input
    const nameContainer = document.createElement('div');
    nameContainer.className = 'col-md-6';

    const nameInput = document.createElement('input')
    nameInput.className = 'form-control'
    nameInput.id = `field${fieldCount}`;
    nameInput.type = 'text';
    nameInput.placeholder = 'field name';
    nameInput.required = true;

    // append input to container and container to row
    nameContainer.appendChild(nameInput);
    rowElement.appendChild(nameContainer);

    // create type selector
    const typeContainer = document.createElement('div');
    typeContainer.className = 'col-md-3';

    const typeSelect = document.createElement('select');
    typeSelect.className = 'form-select';
    typeSelect.ariaLabel = 'field type';
    typeSelect.required = true;

    // create options
    const defaultOpt = document.createElement('option');
    defaultOpt.selected = true;
    defaultOpt.value = '';
    defaultOpt.innerText = 'field type';
    typeSelect.appendChild(defaultOpt);

    typeOptions.forEach((option) => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.innerText = option;

        typeSelect.appendChild(opt);
    })

    typeContainer.appendChild(typeSelect);
    rowElement.appendChild(typeContainer);

    // Create delete button
    const buttonContainer = document.createElement('div');
    buttonContainer.className = 'col-md-3 d-flex flex-column align-items-end';

    const deleteButton = document.createElement('button');
    deleteButton.className = 'btn btn-danger';
    deleteButton.innerText = 'Remove';
    deleteButton.addEventListener('click', (ev) => {
        ev.preventDefault();
        fieldList.removeChild(rowElement);
    });

    // Add button to button container and the container to the row
    buttonContainer.appendChild(deleteButton);
    rowElement.appendChild(buttonContainer);

    // Add finished element to field list
    fieldList.appendChild(rowElement);
    fieldCount++;
};

document.getElementById('addField').addEventListener('click', (ev) => {
    ev.preventDefault();
    addField();
});

const form = document.getElementById('createForm') as HTMLFormElement;

form.addEventListener('formdata', (ev) => {
    const formData = ev.formData;

    const fieldData = {};

    fieldList.querySelectorAll('.row.field').forEach((field: HTMLDivElement) => {
        const fieldName = field.querySelector('input').value;
        const fieldValue = field.querySelector('select').value;
        fieldData[fieldName] = fieldValue;
    });

    formData.append('fields', JSON.stringify(fieldData));
})

// add first field
addField();
