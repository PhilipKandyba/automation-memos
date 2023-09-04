from core.web.entities.browser_element import BrowserElement
from core.web.wrappers import page
from core import by


@page(url="/auth")
class NavigationElement:
    USERNAME_LABEL: BrowserElement = (
        by.CSS_SELECTOR,
        "header .px-1.text-lg",
    )
