import flet as ft

def stakeholder_check_ex(page):

    stakeholder_check1_ex = ft.View(
        "/stakeholder_check1_ex",
        [
            ft.AppBar(
                title=ft.Text("사적이해관계자 Checklist 1"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 상대 **공직자**가 수행하는 업무가 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "보조금·장려금·출연금·출자금·교부금·기금의 배정·지급·처분·관리에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "공사·용역 또는 물품 등의 조달·구매의 계약·검사·검수에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "사건의 수사·재판·심판·결정·조정·중재·화해 또는 이에 준하는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "공공기관의 재화 또는 용역의 매각·교환·사용·수익·점유에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "공직자의 채용·승진·전보·상벌·평가에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "공공기관이 실시하는 행정감사에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "공공기관이 주관하는 각종 수상, 포상, 우수기관 선정, 우수자 선발에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "공공기관이 실시하는 각종 평가·판정에 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "국회의원 또는 지방의회의원의 소관 위원회 활동과 관련된 청문, 의안·청원심사, 국정감사, 지방자치단체의 행정사무감사, 국정조사, 지방자치단체의　행정사무조사와 관계되는 직무",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check2_ex"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/stakeholder_ok_ex")
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

    stakeholder_check2_ex = ft.View(
        "/stakeholder_check2_ex",
        [
            ft.AppBar(
                title=ft.Text("사적이해관계자 Checklist 2"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 상대 **공직자**가 수행하는 직무가 아래 항목에 해당하나요?", width=500, extension_set=ft.MarkdownExtensionSet.GITHUB_WEB),
            ft.ElevatedButton(
                "직무수행과 관련하여 일정한 행위나 조치를 요구하는 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check3_ex"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check3_ex"),
            ),
            ft.ElevatedButton(
                "자신이 소속된 공공기관과 계약을 체결하거나 체결하려는 것이 명백한 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check3_ex"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 다른 공직자",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check3_ex"),
            ),
            ft.ElevatedButton(
                "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 다른 공직자 다만, 공공기관이 이익 또는 불이익을 직접적으로 받는 경우, 그 공공기관에 소속되어 해당 이익 또는 불이익과 관련된 업무를 담당하는 공직자",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check3_ex"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/stakeholder_ok_ex")
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

    stakeholder_check3_ex = ft.View(
        "/stakeholder_check3_ex",
        [
            ft.AppBar(
                title=ft.Text("사적이해관계자 Checklist 3"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 상대 **공직자**가 수행하는 직무가 아래 항목에 해당하나요?", width=500, extension_set=ft.MarkdownExtensionSet.GITHUB_WEB),
            ft.ElevatedButton(
                "불특정 다수를 대상으로 하는 법률이나 대통령령의 제정·개정 또는 폐지를 수반하는 경우",
                width=500,
                on_click=lambda _: page.go("/stakeholder_ok_ex"),
            ),
            ft.ElevatedButton(
                "특정한 사실 또는 법률관계에 관한 확인·증명을 신청하는 민원에 따라 해당 서류를 발급하는 경우",
                width=500,
                on_click=lambda _: page.go("/stakeholder_ok_ex"),
            ),
            ft.ElevatedButton(
                "다른 법령·기준에 제척·기피·회피 등 이해충돌 방지를 위한 절차가 마련되어 있어 그 절차에 따른 경우",
                width=500,
                on_click=lambda _: page.go("/stakeholder_ok_ex"),
            ),
            ft.ElevatedButton(
                "해당없음",
                width=500,
                on_click=lambda _: page.go("/stakeholder_check4_ex"),
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

    stakeholder_check4_ex = ft.View(
        "/stakeholder_check4_ex",
        [
            ft.AppBar(
                title=ft.Text("사적이해관계자 Checklist 4"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 본인이 아래 항목에 해당하나요?", width=500),
            ft.ElevatedButton(
                "공직자 또는 그 가족 (「민법」 제779조에 따른 가족을 말한다)",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "공직자 또는 그 가족이 임원·대표자·관리자·사외이사로 재직하고 있는 법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "공직자나 그 가족이 대리하거나 고문·자문 등을 제공하는 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "공직자로 채용·임용되기 전 2년 이내에 공직자 자신이 재직하였던 법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "공직자로 채용·임용되기 전 2년 이내에 공직자 자신이 대리하거나 고문·자문 등을 제공하였던 개인·법인·단체",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "공직자 또는 그 가족이 단독으로 또는 합산하여 다음 각 항목 중 어느 하나에 해당하는 주식·지분 등을 소유하고 있는 법인·단체\n  - 발행주식 총수의 30% 이상, 혹은 출자지분 총수의 30% 이상, 혹은 자본금 총액의 50% 이상",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "퇴직일 전 2년 이내에 실·국·과에서 같이 근무하면서 해당 공직자를 법령·기준·사실상 지휘·감독하였던 최근 2년 이내 퇴직한 공직자\n  * 국회·대법원·헌법재판소·중앙선관위 공직자는 규칙으로 부서의 범위를 별도 규정 가능",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "법령·기준에 따라 공직자를 지휘·감독하는 상급자",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "최근 2년간 1회에 100만원 또는 매 회계연도에 300만원을 초과하는 금전 거래*가 있었던 자(친족 제외)\n  * 금융회사, 대부업자 등으로부터 통상적인 조건으로 금전을 빌리는 행위는 제외",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "공공기관의 장이 해당 공공기관의 업무 특성을 반영하여 공정한 직무 수행에 영향을 미칠 수 있다고 인정하여 정하는 자",
                width=500,
                on_click=lambda _: page.go("/stakeholder_declaration_ex"),
            ),
            ft.ElevatedButton(
                "해당없음", width=500, on_click=lambda _: page.go("/stakeholder_ok_ex")
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

    stakeholder_ok_ex = ft.View(
        "/stakeholder_ok_ex",
        [
            ft.AppBar(
                title=ft.Text("사적이해관계자 신고·회피 의무 불요"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Markdown("## 사적이해관계자 신고·회피 의무가 없습니다."),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/external"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    stakeholder_declaration_ex = ft.View(
        "/stakeholder_declaration_ex",
        [
            ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.RED),
            ft.Markdown("## 사적이해관계자 신고 조치가 **필요**합니다."),
            ft.Markdown(
                """
신고방법: 직무관련자가 사적이해관계자로 확인된 경우, 안 날로 부터 14일 이내 '공공기관 청렴포털 시스템'에 의무신고
- 퇴직자 사적접촉, 직무관련자와의 거래 행위 등도 그 사실을 '안 날'부터 14일 이내 신고
※ 상담신고처: 공공기관 청렴포털 시스템([www.clean.go.kr](www.clean.go.kr)) 혹은 compliance@koica.go.kr
""", extension_set=ft.MarkdownExtensionSet.GITHUB_WEB
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

    stakeholder_routes_ex = {
        "/stakeholder_check1_ex": stakeholder_check1_ex,
        "/stakeholder_check2_ex": stakeholder_check2_ex,
        "/stakeholder_check3_ex": stakeholder_check3_ex,
        "/stakeholder_check4_ex": stakeholder_check4_ex,
        "/stakeholder_ok_ex": stakeholder_ok_ex,
        "/stakeholder_declaration_ex": stakeholder_declaration_ex,
    }

    return stakeholder_routes_ex