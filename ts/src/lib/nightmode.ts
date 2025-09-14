export function checkNightMode(): boolean {
    const nightMode = window.location.hash == "#night";
    if (nightMode) {
        document.documentElement.className = "night-mode";
        document.documentElement.dataset.bsTheme = "dark";
    }
    return nightMode;
}
