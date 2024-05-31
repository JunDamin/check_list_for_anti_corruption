# %%
import flet as ft
from presents_check import present_check
from presents_check_ex import present_check_ex
from stakeholders_check import stakeholder_check
from stakeholders_check_ex import stakeholder_check_ex
from job_related_check import job_related_check
from job_related_check_ex import job_related_check_ex
from retired_check import retired_check
from retired_check_ex import retired_check_ex
from lecture_declaration import lecture_check


# %%
def main(page: ft.Page):
    page.title = "반부패 이해충돌 방지 자가진단 체크리스트"

    def route_change(route):
        page.views.clear()

        home = ft.View(
            "/",
            [
                ft.AppBar(
                    title=ft.Text("반부패 자가진단 체크리스트"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.PUBLIC),
                            ft.Text(
                                "공직자(공무수행사인)입니다.",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    width=500,
                    on_click=lambda _: page.go("/internal"),
                    height=50,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.PRIVACY_TIP),
                            ft.Text(
                                "공직자(공무수행사인)가 아닙니다.",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    width=500,
                    on_click=lambda _: page.go("/external"),
                    height=50,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        internal = ft.View(
            "/internal",
            [
                ft.AppBar(
                    title=ft.Text("반부패 자가진단 체크리스트"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "수수금지 음식물 선물 경조사비 자가 진단 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/present_check1"),
                    icon=ft.icons.CARD_GIFTCARD,
                    height=50,
                ),
                ft.ElevatedButton(
                    "사적이해관계자의 신고·회피 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check1"),
                    icon=ft.icons.PEOPLE_OUTLINE,
                    height=50,
                ),
                ft.ElevatedButton(
                    "직무관련자와의 거래 신고 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/job_related_check1"),
                    icon=ft.icons.HANDSHAKE,
                    height=50,
                ),
                ft.ElevatedButton(
                    "퇴직자 사적접촉 신고 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/retired_check1"),
                    icon=ft.icons.ACCESSIBILITY,
                    height=50,
                ),
                ft.ElevatedButton(
                    "외부강의등 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/lecture_intro1"),
                    icon=ft.icons.ACCESSIBILITY,
                    height=50,
                ),
                ft.FilledButton(
                    "사용자 변경하기",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        external = ft.View(
            "/external",
            [
                ft.AppBar(
                    title=ft.Text("반부패 자가진단 체크리스트"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "수수금지 음식물 선물 경조사비 자가 진단 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/present_check1_ex"),
                    icon=ft.icons.CARD_GIFTCARD,
                    height=50,
                ),
                ft.ElevatedButton(
                    "사적이해관계자의 신고·회피 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check1_ex"),
                    icon=ft.icons.PEOPLE_OUTLINE,
                    height=50,
                ),
                ft.ElevatedButton(
                    "직무관련자와의 거래 신고 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/job_related_check1_ex"),
                    icon=ft.icons.HANDSHAKE,
                    height=50,
                ),
                ft.ElevatedButton(
                    "퇴직자 사적접촉 신고 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/retired_check1_ex"),
                    icon=ft.icons.ACCESSIBILITY,
                    height=50,
                ),
                ft.FilledButton(
                    "사용자 변경하기",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        routes = {
            "/": home,
            "/internal": internal,
            "/external": external,
        }

        present_routes = present_check(page)
        stakeholder_routes = stakeholder_check(page)
        job_related_routes = job_related_check(page)
        retired_routes = retired_check(page)
        lecture_routes = lecture_check(page)

        preesent_routes_ex = present_check_ex(page)
        stakeholder_routes_ex = stakeholder_check_ex(page)
        job_related_routes_ex = job_related_check_ex(page)
        retired_routes_ex = retired_check_ex(page)

        routes.update(present_routes)
        routes.update(preesent_routes_ex)
        routes.update(stakeholder_routes)
        routes.update(stakeholder_routes_ex)
        routes.update(job_related_routes)
        routes.update(job_related_routes_ex)
        routes.update(retired_routes)
        routes.update(retired_routes_ex)
        routes.update(lecture_routes)

        page.views.append(routes.get(page.route, "/"))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
# %%
