function updateBatteryStatus(battery) {
    const batteryPercentage = Math.round(battery.level * 100);
    const charging = battery.charging;
    const inputWatt = 150; // Charger wattage in W
    const capacity_mWh = 80000; // Battery capacity in mWh

    const batteryLevelEl = document.getElementById("battery-level");
    const chargingStatusEl = document.getElementById("charging-status");
    const chargingRateEl = document.getElementById("charging-rate");
    const chargingTimeEl = document.getElementById("charging-time");
    const progressBar = document.getElementById("progress-bar");

    // Update battery percentage
    batteryLevelEl.textContent = `Battery Percentage: ${batteryPercentage}%`;
    progressBar.style.width = `${batteryPercentage}%`;

    // Update charging status
    chargingStatusEl.textContent = `Charging Status: ${charging ? "Plugged In" : "Not Charging"}`;
    chargingStatusEl.className = charging ? "charging" : "not-charging";

    // Low battery warning
    if (batteryPercentage <= 15 && !charging) {
        batteryLevelEl.classList.add("low-battery");
        alert("⚠️ Warning: Low Battery! Please plug in your charger.");
    } else {
        batteryLevelEl.classList.remove("low-battery");
    }

    // Calculate estimated charging rate and time
    if (charging) {
        const chargeRate = (inputWatt / (capacity_mWh / 1000)).toFixed(2); // percentage/hour
        chargingRateEl.textContent = `Estimated Charging Rate: ${chargeRate}% per hour`;

        const remainingPercent = 100 - batteryPercentage;
        const timeToFull = (remainingPercent / chargeRate).toFixed(1); // hours
        chargingTimeEl.textContent = `Time to Full Charge: ${timeToFull} hours`;
    } else {
        chargingRateEl.textContent = "Estimated Charging Rate: --";
        chargingTimeEl.textContent = "Time to Full Charge: --";
    }
}

// Battery API support check
if ("getBattery" in navigator) {
    navigator.getBattery().then(battery => {
        // Initial update
        updateBatteryStatus(battery);

        // Listen for changes
        battery.addEventListener("chargingchange", () => updateBatteryStatus(battery));
        battery.addEventListener("levelchange", () => updateBatteryStatus(battery));

        // Auto-refresh every 5 seconds
        setInterval(() => {
            updateBatteryStatus(battery);
        }, 5000); // 5000ms = 5 seconds
    });
} else {
    document.getElementById("battery-level").textContent =
        "Battery API not supported in this browser.";
}
