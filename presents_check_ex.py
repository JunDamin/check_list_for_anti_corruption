import flet as ft


def present_check_ex(page):
    present_check1_ex = ft.View(
        "/present_check1_ex",
        [
            ft.AppBar(
                title=ft.Text("Checklist 1 가액 자가 진단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 제공하고자 하는 금품의 가격이 어떻게 되나요?", width=500),
            ft.ElevatedButton(
                "1회 100만원(회계연도 300만원) 초과",
                width=500,
                on_click=lambda _: page.go("/present_check3_ex"),
            ),
            ft.ElevatedButton(
                "1회 100만원 이하",
                width=500,
                on_click=lambda _: page.go("/present_check2_ex"),
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    present_check2_ex = ft.View(
        "/present_check2_ex",
        [
            ft.AppBar(
                title=ft.Text("Checklist 2 직무관련성 자가진단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 선물한 사람과의 관계가 어떻게 되나요?\n"),
            ft.Column(
                [
                    ft.Text("(1) 직무 관련자"),
                    ft.ElevatedButton(
                        "기관에 민원 사무를 신청하는 중이거나 신청하려는 것이 명백한 개인 또는 법인, 단체",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "인허가, 검사, 감사, 단속, 지도 등의 대상인 개인 또는 법인, 단체",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "결정, 감정, 시험, 사정, 조정 등으로 이익 또는 불이익을 직접적으로 받는 개인 또는 법인, 단체",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "수사, 감사, 감독, 검사, 단속, 행정지도 또는 이에 준하는 업무 절차에 따라 이익 또는 불이익을 받는 법인, 단체 또는 개인",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "기관과 계약을 체결하거나 체결하려는 것이 명백한 개인 또는 법인, 단체",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "기타 기관에 대하여 특정한 행위를 요구하거나, 임직원의 직무상 권한의 행사 또는 불행사로 금전적 이해관계에 영향을 받는 개인 또는 법인, 단체",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "정책, 사업 등의 결정 또는 집행으로 직접 이익 또는 불이익을 받는 개인 또는 법인, 단체",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Text("(2) 직무 관련 임직원"),
                    ft.ElevatedButton(
                        "임직원의 소관 업무와 관련하여 직무상 명령을 받는 하급자",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "인사, 예산, 감사, 상훈 또는 평가 등의 직무를 수행하는 임직원",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "사무를 위임, 위탁한 경우 그 사무의 위임, 위탁을 받은 임직원",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                    ft.ElevatedButton(
                        "기타 기관장이 정하는 임직원",
                        width=500,
                        on_click=lambda _: page.go("/present_check3_ex"),
                    ),
                ]
            ),
            ft.ElevatedButton(
                "해당되는 사항이 없습니다.",
                width=500,
                on_click=lambda _: page.go("/present_check_ok_ex"),
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    present_check3_ex = ft.View(
        "/present_check3_ex",
        [
            ft.AppBar(
                title=ft.Text("Checklist 3 수수 금지 금품 등의 예외사유 해당여부 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 아래 예외사유에 해당하나요?"),
            ft.ElevatedButton(
                "공공기관의 장이 소속 임직원이나 파견 임직원에게 지급하는 경우",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "상급자가 위로, 격려, 포상 등의 목적으로 하급자에게 제공하는 경우",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "원활한 직무수행 또는 사교, 의례의 목적으로 제공되는 음식물, 경조사비, 선물 등으로 허용 가액 범위 내에 해당하는 금액",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.Text(
                """<가액범위> 
- 음식물은 3만원 이하
- 선물은 5만원 이하 (단, 농산물, 농수산가공품은 명절(설날, 추석) 전 24일 부터 후 5일까지 20만원, 그 외 기간은 10만원)
- 경조사비는 5만원 이하(단, 화환, 조화의 경우 10만원)""",
                width=500,
            ),
            ft.ElevatedButton(
                "임직원의 친족(「민법」 제777조 기준)이 제공하는 음식물, 선물, 경조사비",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "임직원과 관련된 직원상조회, 동호인회, 동창회, 향우회, 친목회, 종교단체, 사회단체 등이 정하는 기준에 따라 구성원에게 제공하는 음식물, 선물, 경조사비",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "임직원과 특별히 장기적, 지속적인 친분관계를 맺고 있는 자가 질병, 재난 등으로 어려운 처지에 있는 공직자 등에게 제공하는 음식물, 선물, 경조사비",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "공직자 등의 직무와 관련된 공식적인 행사에서 주최자가 참석자에게 통상적인 범위에서 일률적으로 제공하는 음식물",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "불특정 다수인에게 배포하기 위한 기념품 또는 홍보용품 등이나 경연, 추첨을 통하여 받는 보상 또는 경품 등",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "그밖에 다른 법령 기준 또는 사회상규에 따라 허용되는 음식물, 선물, 경조사비",
                width=500,
                on_click=lambda _: page.go("/present_check_exception_ex"),
            ),
            ft.ElevatedButton(
                "해당되는 사항이 없습니다.",
                width=500,
                on_click=lambda _: page.go("/present_declaration_ex"),
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    present_check_exception_ex = ft.View(
        "/present_check_exception_ex",
        [
            ft.AppBar(title=ft.Text("선물수수 허용"), bgcolor=ft.colors.GREEN),
            ft.Markdown("## 예외사유에 해당되어 선물수수가 가능합니다."),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    present_check_ok = ft.View(
        "/present_check_ok_ex",
        [
            ft.AppBar(title=ft.Text("선물수수 허용"), bgcolor=ft.colors.GREEN),
            ft.Markdown(
                "직무관련성이 없는 경우에 한해 1회 100만원 이하의 선물수수가 허용됩니다."
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    present_declaration_ex = ft.View(
        "/present_declaration_ex",
        [
            ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.RED),
            ft.Markdown(
                "선물수수가 불가하여 **신고 조치가 필요**합니다.",
                auto_follow_links=True,
            ),
            ft.Markdown(
                """
신고방법: 직무관련자가 사적이해관계자로 확인된 경우, 안 날로 부터 14일 이내 '공공기관 청렴포털 시스템'에 의무신고
- 퇴직자 사적접촉, 직무관련자와의 거래 행위 등도 그 사실을 '안 날'부터 14일 이내 신고
※ 상담신고처: 공공기관 청렴포털 시스템(www.clean.go.kr) 혹은 compliance@koica.go.kr
""",
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                auto_follow_links=True,
            ),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    ## 공식행사 체크리스트 추가 필요

    preesent_routes_ex = {
        "/present_check1_ex": present_check1_ex,
        "/present_check2_ex": present_check2_ex,
        "/present_check3_ex": present_check3_ex,
        "/present_check_ok_ex": present_check_ok,
        "/present_check_exception_ex": present_check_exception_ex,
        "/present_declaration_ex": present_declaration_ex,
    }

    return preesent_routes_ex
