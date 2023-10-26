import flet as ft
from retired_check_ex import retired_check_ex

def retired_check(page):

    retired_check1 = ft.View(
        "/retired_check1",
        [
            ft.AppBar(
                title=ft.Text("퇴직자 사적접촉 Checklist 1"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Text("퇴직자 사적 접촉과 관련하여 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "퇴직자의 신분이 공직자가 아니게 된 날부터 2년이 지난 경우",
                width=500,
                on_click=lambda _: page.go("/retired_ok"),
            ),
            ft.ElevatedButton(
                "사회상규에 따라 허용되는 경우로 퇴직자를 접촉한 경우",
                width=500,
                on_click=lambda _: page.go("/retired_ok"),
            ),
            ft.ElevatedButton(
                "퇴직자 자녀의 결혼식, 돌잔치, 환갑 등 경조사에서 퇴직자를 부득이 접촉한 경우",
                width=500,
                on_click=lambda _: page.go("/retired_ok"),
            ),
            ft.ElevatedButton(
                "직무와 무관한 동창회, 친목 모임, 종교행사 등의 사적 모임에서 퇴직자를 부득이 접촉한 경우",
                width=500,
                on_click=lambda _: page.go("/retired_ok"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/retired_check2")
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    retired_check2 = ft.View(
        "/retired_check2",
        [
            ft.AppBar(
                title=ft.Text("퇴직자 사적접촉 Checklist 2"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Text("퇴직자 사적 접촉 유형이 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "골프를 함께하는 행위",
                width=500,
                on_click=lambda _: page.go("/retired_check3"),
            ),
            ft.ElevatedButton(
                "여행을 함께하는 행위",
                width=500,
                on_click=lambda _: page.go("/retired_check3"),
            ),
            ft.ElevatedButton(
                "사행성 오락을 함께 하는 행위",
                width=500,
                on_click=lambda _: page.go("/retired_check3"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/retired_ok")
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    retired_check3 = ft.View(
        "/retired_check3",
        [
            ft.AppBar(
                title=ft.Text("퇴직자 사적접촉 Checklist 3"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Text("사적 접촉 퇴직자가 자신이 수행하고 있는 직무와 관련 되는자로 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "직무수행과 관련하여 일정한 행위나 조치를 요구하는 개인이나 법인 또는 단체",
                width=500,
                on_click=lambda _: page.go("/retired_declaration"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 개인이나 법인 또는 단체",
                width=500,
                on_click=lambda _: page.go("/retired_declaration"),
            ),
            ft.ElevatedButton(
                "자신이 소속된 공공기관과 계약을 체결하거나 체결하려는 것이 명백한 개인이나 법인 또는 단체",
                width=500,
                on_click=lambda _: page.go("/retired_declaration"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 다른 공직자. 다만, 공공기관이 이익 또는 불이익을 직접적으로 받는 경우, 그 공공기관에 소속되어 해당 이익 또는 불이익과 관련된 업무를 담당하는 공직자",
                width=500,
                on_click=lambda _: page.go("/retired_declaration"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/retired_ok")
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    retired_ok = ft.View(
        "/retired_ok",
        [
            ft.AppBar(
                title=ft.Text("신고·회피 의무 불요"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Text("퇴직자 사적접촉 신고·회피 의무가 없습니다."),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    retired_declaration = ft.View(
        "/retired_declaration",
        [
            ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.RED),
            ft.Text("퇴직자 사적 접촉 신고 조치가 필요합니다."),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    retired_routes = {
        "/retired_check1": retired_check1,
        "/retired_check2": retired_check2,
        "/retired_check3": retired_check3,
        "/retired_ok": retired_ok,
        "/retired_declaration": retired_declaration,
    }



    return retired_routes