# %%
import flet as ft
from presents_check import present_check
from stakeholders_check import stakeholder_check
from job_related_check import job_related_check
from retired_check import retired_check


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
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        #
        #
        #

        ###
        #
        ###
        

        ###
        #
        ###

        

        routes = {
            "/": home,
        }

        present_routes = present_check(page)
        stakeholder_routes = stakeholder_check(page)
        job_related_routes = job_related_check(page)
        retired_routes = retired_check(page)

        routes.update(present_routes)
        routes.update(stakeholder_routes)
        routes.update(job_related_routes)
        routes.update(retired_routes)

        page.views.append(routes.get(page.route, "/"))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets")
# %%
