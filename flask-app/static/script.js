
const brandDropdown = document.getElementById("brand");
const modelDropdown = document.getElementById("car_model");

// Get car models whenever brand changes
brandDropdown.addEventListener("change", async function () {

    const brand = this.value;

    modelDropdown.innerHTML = '<option value="">Select Car Model</option>';

    clearSpecifications();

    if (!brand) {
        return;
    }

    try {
        const response = await fetch(
            `/get_models/${encodeURIComponent(brand)}`
        );

        const models = await response.json();

        models.forEach(function (model) {
            const option = document.createElement("option");

            option.value = model;
            option.textContent = model;

            modelDropdown.appendChild(option);
        });

    } catch (error) {
        console.error("Error loading car models:", error);
    }
});


// Get specifications whenever car model changes
modelDropdown.addEventListener("change", async function () {

    const carName = this.value;

    clearSpecifications();

    if (!carName) {
        return;
    }

    try {
        const response = await fetch(
            `/get_car_specs?name=${encodeURIComponent(carName)}`
        );

        if (!response.ok) {
            throw new Error("Car specifications not found");
        }

        const specs = await response.json();

        document.getElementById("fuel_type").value = specs.Fuel_Type;
        document.getElementById("transmission").value = specs.Transmission;
        document.getElementById("mileage").value = specs.Mileage;
        document.getElementById("engine").value = specs.Engine;
        document.getElementById("power").value = specs.Power;
        document.getElementById("seats").value = specs.Seats;

    } catch (error) {
        console.error("Error loading car specifications:", error);
    }
});


// Clear old specifications
function clearSpecifications() {

    document.getElementById("fuel_type").value = "";
    document.getElementById("transmission").value = "";
    document.getElementById("mileage").value = "";
    document.getElementById("engine").value = "";
    document.getElementById("power").value = "";
    document.getElementById("seats").value = "";
}
