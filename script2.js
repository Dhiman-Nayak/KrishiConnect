document.addEventListener('DOMContentLoaded', () => {
    const sunlightValue = document.getElementById('sunlight-value');
    const generateButton = document.getElementById('generate-button');

    generateButton.addEventListener('click', () => {
        // Generate a random sunlight value between 0 and 10000 lx
        const randomSunlight = Math.floor(Math.random() * 10001);
        sunlightValue.innerText = randomSunlight + ' lx';
    });
});
