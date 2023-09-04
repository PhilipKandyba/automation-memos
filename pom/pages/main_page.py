from core import by
from core.web.wrappers import page
from core.web.entities.browser_element import BrowserElement, Locator


@page(url="/")
class MainPage:
    EDITOR_CONTAINER: Locator | BrowserElement = Locator(
        by.CSS_SELECTOR,
        ".memo-editor-container",
    )
    LATEST_MEMO_ITEM: Locator | BrowserElement = Locator(
        by.CSS_SELECTOR, ".memo-wrapper:first-child"
    )
    LATEST_MEMO_ITEM_CONTENT: BrowserElement = LATEST_MEMO_ITEM.extend(
        ".memo-content-text"
    )
    LATEST_MEMO_ITEM_SUBMENU: BrowserElement = LATEST_MEMO_ITEM.extend(
        ".more-action-btn"
    )

    EDITOR_INPUTER: BrowserElement = by.CSS_SELECTOR, ".common-editor-inputer"
    EDITOR_SUBMIT_BUTTON: BrowserElement = EDITOR_CONTAINER.extend(
        "button.confirm-btn"
    )

    MEMO_ITEM_SUBMENU_DELETE_BUTTON: BrowserElement = (
        by.CSS_SELECTOR,
        ".text-red-600",
    )
    MEMO_ITEM_SUBMENU_EDIT_BUTTON: BrowserElement = (
        by.XPATH,
        "//span[contains(text(), 'Edit')]",
    )
