export function checkNightMode(): boolean {
    const nightMode = window.location.hash == "#night";
    if (nightMode) {
        document.documentElement.className = "night-mode";
        document.documentElement.dataset.bsTheme = "dark";
    }
    return nightMode;
}

export interface ThemeInfo {
    isDark: boolean;
}

function getThemeFromRoot(): ThemeInfo {
    return {
        isDark: document.documentElement.classList.contains("night-mode"),
    };
}

export const pageTheme = $state(getThemeFromRoot());

const observer = new MutationObserver((_mutationsList, _observer) => {
    pageTheme.isDark = getThemeFromRoot().isDark;
});
observer.observe(document.documentElement, { attributeFilter: ["class"] });
