import flet as ft
from job_related_check_ex import job_related_check_ex


def job_related_check(page):
    job_related_check1 = ft.View(
        "/job_related_check1",
        [
            ft.AppBar(
                title=ft.Text("직무관련자와의 거래 Checklist 1"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 거래 상대방이 자신이 수행하고 있는 직무와 관련되는 자로 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "직무수행과 관련하여 일정한 행위나 조치를 요구하는 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/job_related_check2"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/job_related_check2"),
            ),
            ft.ElevatedButton(
                "자신이 소속된 공공기관과 계약을 체결하거나 체결하려는 것이 명백한 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/job_related_check2"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받거나, 업무 유관성이 있는 공직자",
                width=500,
                on_click=lambda _: page.go("/job_related_check2"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 다른 공직자 다만, 공공기관이 이익 또는 불이익을 직접적으로 받는 경우, 그 공공기관에 소속되어 해당 이익 또는 불이익과 관련된 업무를 담당하는 공직자",
                width=500,
                on_click=lambda _: page.go("/job_related_check2"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/job_related_ok")
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

    job_related_check2 = ft.View(
        "/job_related_check2",
        [
            ft.AppBar(
                title=ft.Text("직무관련자와의 거래 Checklist 2"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## **직무관련자**와 거래한 자가 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "공직자 자신",
                width=500,
                on_click=lambda _: page.go("/job_related_check3"),
            ),
            ft.ElevatedButton(
                "공직자의 직계존속 또는 직계비속",
                width=500,
                on_click=lambda _: page.go("/job_related_check3"),
            ),
            ft.ElevatedButton(
                "공직자의 배우자",
                width=500,
                on_click=lambda _: page.go("/job_related_check3"),
            ),
            ft.ElevatedButton(
                "생계를 같이하는 공직자 배우자의 직계존속·비속",
                width=500,
                on_click=lambda _: page.go("/job_related_check3"),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "공직자 자신, 배우자, 직계존속·비속, 생계를 같이 하는 배우자의 직계존속·비속이 단독으로 또는 합산하여 다음 각 항목 중 어느 하나에 해당하는 주식·지분 등을 소유하고 있는 법인·단체의 ",
                            width=500,
                        ),
                        ft.ElevatedButton(
                            "발행주식 총수의 30% 이상",
                            width=500,
                            on_click=lambda _: page.go("/job_related_check3"),
                        ),
                        ft.ElevatedButton(
                            "출자지분 총수의 30% 이상",
                            width=500,
                            on_click=lambda _: page.go("/job_related_check3"),
                        ),
                        ft.ElevatedButton(
                            "자본금 총액의 50% 이상",
                            width=500,
                            on_click=lambda _: page.go("/job_related_check3"),
                        ),
                    ],
                ),
                bgcolor=ft.colors.TEAL_ACCENT,
                padding=10,
                border_radius=20,
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/job_related_ok")
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

    job_related_check3 = ft.View(
        "/job_related_check3",
        [
            ft.AppBar(
                title=ft.Text("직무관련자와의 거래 Checklist 3"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 거래 행위가 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "금전을 빌리거나 빌려주는 행위 및 유가증권을 거래하는 행위",
                width=500,
                on_click=lambda _: page.go("/job_related_check4"),
            ),
            ft.ElevatedButton(
                "토지 또는 건축물 등 부동산을 거래하는 행위",
                width=500,
                on_click=lambda _: page.go("/job_related_check4"),
            ),
            ft.ElevatedButton(
                "그 외의 물품·용역·공사 등의 계약을 체결하는 행위\n(1회 100만원이 초과하고 계약서를 작성하는 중고거래(차량 판매 등))",
                width=500,
                on_click=lambda _: page.go("/job_related_check4"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/job_related_ok")
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
    job_related_check4 = ft.View(
        "/job_related_check4",
        [
            ft.AppBar(
                title=ft.Text("직무관련자와의 거래 Checklist 4"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## **직무관련자**와 거래한 자가 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "직무관련자가 「민법」 제777조에 따른 친족인 경우",
                width=500,
                on_click=lambda _: page.go("/job_related_ok"),
            ),
            ft.ElevatedButton(
                "「금융실명법」에 따른 금융회사 등, 「대부업법」에 따른 대부업자등이나 그 밖의 금융회사로부터 통상적인 조건으로 금전을 빌리는 행위 및 유가증권을 거래하는 행위인 경우",
                width=500,
                on_click=lambda _: page.go("/job_related_ok"),
            ),
            ft.ElevatedButton(
                "공개모집에 의한 분양이나 공매·경매·입찰을 통한 재산상 거래 행위인 경우",
                width=500,
                on_click=lambda _: page.go("/job_related_ok"),
            ),
            ft.ElevatedButton(
                "공매·경매·입찰을 통한 계약 체결 행위 또는 거래관행상 불특정 다수를 대상으로 반복적으로 행하여지는 계약 체결 행위인 경우",
                width=500,
                on_click=lambda _: page.go("/job_related_ok"),
            ),
            ft.ElevatedButton(
                "해당없음",
                width=500,
                on_click=lambda _: page.go("/job_related_declaration"),
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

    job_related_ok = ft.View(
        "/job_related_ok",
        [
            ft.AppBar(
                title=ft.Text("신고·회피 의무 불요"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Markdown("## 직무관련자와의 거래 신고·회피 의무가 없어 종료"),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    job_related_declaration = ft.View(
        "/job_related_declaration",
        [
            ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.RED),
            ft.Markdown("## 직무관련자와의 거래로 신고 조치가 필요합니다."),
            ft.Markdown(
                """
신고방법: 직무관련자가 사적이해관계자로 확인된 경우, 안 날로 부터 14일 이내 '공공기관 청렴포털 시스템'에 의무신고
- 퇴직자 사적접촉, 직무관련자와의 거래 행위 등도 그 사실을 '안 날'부터 14일 이내 신고
※ 상담신고처: 공공기관 청렴포털 시스템(www.clean.go.kr) 혹은 compliance@koica.go.kr
""",
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB, auto_follow_links=True
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

    job_related_routes = {
        "/job_related_check1": job_related_check1,
        "/job_related_check2": job_related_check2,
        "/job_related_check3": job_related_check3,
        "/job_related_check4": job_related_check4,
        "/job_related_ok": job_related_ok,
        "/job_related_declaration": job_related_declaration,
    }

    return job_related_routes
