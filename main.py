# %%
import flet as ft


# %%
def main(page: ft.Page):
    page.title = ""

    def route_change(route):
        page.views.clear()

        home = ft.View(
            "/",
            [
                ft.AppBar(
                    title=ft.Text("반부패 이해충돌 방지 자가진단 체크리스트"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "수수금지 음식물 선물 경조사비 자가 진단 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/present_check1"),
                ),
                ft.ElevatedButton(
                    "사적이해관계자의 신고·회피 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check1"),
                ),
                ft.ElevatedButton(
                    "직무관련자와의 거래 신고 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/job_related_check1"),
                ),
                ft.ElevatedButton(
                    "퇴직자 사적접촉 신고 의무 체크리스트",
                    width=500,
                    on_click=lambda _: page.go("/retired_check1"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        present_check1 = ft.View(
            "/present_check1",
            [
                ft.AppBar(
                    title=ft.Text("Checklist 1 가액 자가 진단"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "1회 100만원(회계연도 300만원) 초과",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "1회 100만원 이하",
                    width=500,
                    on_click=lambda _: page.go("/present_check2"),
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
                
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        present_check2 = ft.View(
            "/present_check2",
            [
                ft.AppBar(
                    title=ft.Text("Checklist 2 직무관련성 자가진단"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("(1) 직무 관련자"),
                ft.ElevatedButton(
                    "기관에 민원 사무를 신청하는 중이거나 신청하려는 것이 명백한 개인 또는 법인, 단체",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "인허가, 검사, 감사, 단속, 지도 등의 대상인 개인 또는 법인, 단체",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "결정, 감정, 시험, 사정, 조정 등으로 이익 또는 불이익을 직접적으로 받는 개인 또는 법인, 단체",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "수사, 감사, 감독, 검사, 단속, 행정지도 또는 이에 준하는 업무 절차에 따라 이익 또는 불이익을 받는 법인, 단체 또는 개인",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "기관과 계약을 체결하거나 체결하려는 것이 명백한 개인 또는 법인, 단체",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "기타 기관에 대하여 특정한 행위를 요구하거나, 임직원의 직무상 권한의 행사 또는 불행사로 금전적 이해관계에 영향을 받는 개인 또는 법인, 단체",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "정책, 사업 등의 결정 또는 집행으로 직접 이익 또는 불이익을 받는 개인 또는 법인, 단체",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.Text("(2) 직무 관련 임직원"),
                ft.ElevatedButton(
                    "임직원의 소관 업무와 관련하여 직무상 명령을 받는 하급자",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "인사, 예산, 감사, 상훈 또는 평가 등의 직무를 수행하는 임직원",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "사무를 위임, 위탁한 경우 그 사무의 위임, 위탁을 받은 임직원",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "기타 기관장이 정하는 임직원",
                    width=500,
                    on_click=lambda _: page.go("/present_check3"),
                ),
                ft.ElevatedButton(
                    "해당되는 사항이 없습니다.",
                    width=500,
                    on_click=lambda _: page.go("/present_check_ok"),
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        present_check3 = ft.View(
            "/present_check3",
            [
                ft.AppBar(
                    title=ft.Text("Checklist 3 수수 금지 금품 등의 예외사유 해당여부 판단"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "공공기관의 장이 소속 임직원이나 파견 임직원에게 지급하는 경우",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "상급자가 위로, 격려, 포상 등의 목적으로 하급자에게 제공하는 경우",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "원활한 직무수행 또는 사교, 의례의 목적으로 제공되는 음식물, 경조사비, 선물 등으로 허용 가액 범위 내에 해당하는 금액",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
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
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "임직원과 관련된 직원상조회, 동호인회, 동창회, 향우회, 친목회, 종교단체, 사회단체 등이 정하는 기준에 따라 구성원에게 제공하는 음식물, 선물, 경조사비",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "임직원과 특별히 장기적, 지속적인 친분관계를 맺고 있는 자가 질병, 재난 등으로 어려운 처지에 있는 공직자 등에게 제공하는 음식물, 선물, 경조사비",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "공직자 등의 직무와 관련된 공식적인 행사에서 주최자가 참석자에게 통상적인 범위에서 일률적으로 제공하는 음식물",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "불특정 다수인에게 배포하기 위한 기념품 또는 홍보용품 등이나 경연, 추첨을 통하여 받는 보상 또는 경품 등",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "그밖에 다른 법령 기준 또는 사회상규에 따라 허용되는 음식물, 선물, 경조사비",
                    width=500,
                    on_click=lambda _: page.go("/present_check_exception"),
                ),
                ft.ElevatedButton(
                    "해당되는 사항이 없습니다.",
                    width=500,
                    on_click=lambda _: page.go("/present_declaration"),
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        present_check_exception = ft.View(
            "/present_check_exception",
            [
                ft.AppBar(title=ft.Text("선물수수 허용"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("예외사유에 해당되어 선물수수가 가능합니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        present_check_ok = ft.View(
            "/present_check_ok",
            [
                ft.AppBar(title=ft.Text("선물수수 허용"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("직무관련성이 없는 1회 100만원 이하의 선물수수가 허용됩니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        present_declaration = ft.View(
            "/present_declaration",
            [
                ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("선물수수가 불가하여 신고 조치가 필요합니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        ## 공식행사 체크리스트 추가 필요

        preesent_routes = {
            "/present_check1": present_check1,
            "/present_check2": present_check2,
            "/present_check3": present_check3,
            "/present_check_ok": present_check_ok,
            "/present_check_exception": present_check_exception,
            "/present_declaration": present_declaration,
        }

        #
        #
        #

        stakeholder_check1 = ft.View(
            "/stakeholder_check1",
            [
                ft.AppBar(
                    title=ft.Text("사적이해관계자 Checklist 1"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("공직자가 수행하는 업무가 아래 항목에 해당하나요?", width=500),
                ft.ElevatedButton(
                    "보조금·장려금·출연금·출자금·교부금·기금의 배정·지급·처분·관리에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "공사·용역 또는 물품 등의 조달·구매의 계약·검사·검수에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "사건의 수사·재판·심판·결정·조정·중재·화해 또는 이에 준하는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "공공기관의 재화 또는 용역의 매각·교환·사용·수익·점유에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "공직자의 채용·승진·전보·상벌·평가에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "공공기관이 실시하는 행정감사에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "공공기관이 주관하는 각종 수상, 포상, 우수기관 선정, 우수자 선발에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "공공기관이 실시하는 각종 평가·판정에 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "국회의원 또는 지방의회의원의 소관 위원회 활동과 관련된 청문, 의안·청원심사, 국정감사, 지방자치단체의 행정사무감사, 국정조사, 지방자치단체의　행정사무조사와 관계되는 직무",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check2"),
                ),
                ft.ElevatedButton(
                    "해당없음", width=500, on_click=lambda _: page.go("/stakeholder_ok")
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        stakeholder_check2 = ft.View(
            "/stakeholder_check2",
            [
                ft.AppBar(
                    title=ft.Text("사적이해관계자 Checklist 2"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("공직자가 수행하는 직무가 아래 항목에 해당하나요?", width=500),
                ft.ElevatedButton(
                    "직무수행과 관련하여 일정한 행위나 조치를 요구하는 개인·법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check3"),
                ),
                ft.ElevatedButton(
                    "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 개인·법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check3"),
                ),
                ft.ElevatedButton(
                    "자신이 소속된 공공기관과 계약을 체결하거나 체결하려는 것이 명백한 개인·법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check3"),
                ),
                ft.ElevatedButton(
                    "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 다른 공직자",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check3"),
                ),
                ft.ElevatedButton(
                    "직무수행과 관련하여 이익 또는 불이익을 직접적으로 받는 다른 공직자 다만, 공공기관이 이익 또는 불이익을 직접적으로 받는 경우, 그 공공기관에 소속되어 해당 이익 또는 불이익과 관련된 업무를 담당하는 공직자",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check3"),
                ),
                ft.ElevatedButton(
                    "해당없음", width=500, on_click=lambda _: page.go("/stakeholder_ok")
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        stakeholder_check3 = ft.View(
            "/stakeholder_check3",
            [
                ft.AppBar(
                    title=ft.Text("사적이해관계자 Checklist 3"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("공직자가 수행하는 직무가 아래 항목에 해당하나요?", width=500),
                ft.ElevatedButton(
                    "불특정 다수를 대상으로 하는 법률이나 대통령령의 제정·개정 또는 폐지를 수반하는 경우",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_ok"),
                ),
                ft.ElevatedButton(
                    "특정한 사실 또는 법률관계에 관한 확인·증명을 신청하는 민원에 따라 해당 서류를 발급하는 경우",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_ok"),
                ),
                ft.ElevatedButton(
                    "다른 법령·기준에 제척·기피·회피 등 이해충돌 방지를 위한 절차가 마련되어 있어 그 절차에 따른 경우",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_ok"),
                ),
                ft.ElevatedButton(
                    "해당없음",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_check4"),
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        stakeholder_check4 = ft.View(
            "/stakeholder_check4",
            [
                ft.AppBar(
                    title=ft.Text("사적이해관계자 Checklist 4"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("직무관련자가 아래 항목에 해당하나요?", width=500),
                ft.ElevatedButton(
                    "공직자 또는 그 가족 (「민법」 제779조에 따른 가족을 말한다)",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "공직자 또는 그 가족이 임원·대표자·관리자·사외이사로 재직하고 있는 법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "공직자나 그 가족이 대리하거나 고문·자문 등을 제공하는 개인·법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "공직자로 채용·임용되기 전 2년 이내에 공직자 자신이 재직하였던 법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "공직자로 채용·임용되기 전 2년 이내에 공직자 자신이 대리하거나 고문·자문 등을 제공하였던 개인·법인·단체",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "공직자 또는 그 가족이 단독으로 또는 합산하여 다음 각 항목 중 어느 하나에 해당하는 주식·지분 등을 소유하고 있는 법인·단체\n  - 발행주식 총수의 30% 이상, 혹은 출자지분 총수의 30% 이상, 혹은 자본금 총액의 50% 이상",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "퇴직일 전 2년 이내에 실·국·과에서 같이 근무하면서 해당 공직자를 법령·기준·사실상 지휘·감독하였던 최근 2년 이내 퇴직한 공직자\n  * 국회·대법원·헌법재판소·중앙선관위 공직자는 규칙으로 부서의 범위를 별도 규정 가능",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "법령·기준에 따라 공직자를 지휘·감독하는 상급자",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "최근 2년간 1회에 100만원 또는 매 회계연도에 300만원을 초과하는 금전 거래*가 있었던 자(친족 제외)\n  * 금융회사, 대부업자 등으로부터 통상적인 조건으로 금전을 빌리는 행위는 제외",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "공공기관의 장이 해당 공공기관의 업무 특성을 반영하여 공정한 직무 수행에 영향을 미칠 수 있다고 인정하여 정하는 자",
                    width=500,
                    on_click=lambda _: page.go("/stakeholder_declaration"),
                ),
                ft.ElevatedButton(
                    "해당없음", width=500, on_click=lambda _: page.go("/stakeholder_ok")
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        stakeholder_ok = ft.View(
            "/stakeholder_ok",
            [
                ft.AppBar(
                    title=ft.Text("사적이해관계자 신고·회피 의무 불요"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("사적이해관계자 신고·회피 의무가 없습니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        stakeholder_declaration = ft.View(
            "/stakeholder_declaration",
            [
                ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("사적이해관계자 신고 조치가 필요합니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        stakeholder_routes = {
            "/stakeholder_check1": stakeholder_check1,
            "/stakeholder_check2": stakeholder_check2,
            "/stakeholder_check3": stakeholder_check3,
            "/stakeholder_check4": stakeholder_check4,
            "/stakeholder_ok": stakeholder_ok,
            "/stakeholder_declaration": stakeholder_declaration,
        }

        ###
        #
        ###
        job_related_check1 = ft.View(
            "/job_related_check1",
            [
                ft.AppBar(
                    title=ft.Text("직무관련자와의 거래 Checklist 1"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("거래 상대방이 자신이 수행하고 있는 직무와 관련되는 자로 아래 항목에 해당하나요?", width=500),
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
                    on_click=lambda _: page.go("/"),
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
                ft.Text("직무관련자와 거래한 자가 아래 항목에 해당하나요?", width=500),
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
                ft.Text(
                    "공직자 자신, 배우자, 직계존속·비속, 생계를 같이 하는 배우자의 직계존속·비속이 단독으로 또는 합산하여 다음 각 항목 중 어느 하나에 해당하는 주식·지분 등을 소유하고 있는 법인·단체 "
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
                ft.ElevatedButton(
                    "해당없음", width=500, on_click=lambda _: page.go("/job_related_ok")
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
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
                ft.Text("거래 행위가 아래 항목에 해당하나요?", width=500),
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
                    "물품·용역·공사 등의 계약을 체결하는 행위",
                    width=500,
                    on_click=lambda _: page.go("/job_related_check4"),
                ),
                ft.ElevatedButton(
                    "해당없음", width=500, on_click=lambda _: page.go("/job_related_ok")
                ),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
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
                ft.Text("직무관련자와 거래한 자가 아래 항목에 해당하나요?", width=500),
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
                    on_click=lambda _: page.go("/"),
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
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("직무관련자와의 거래 신고·회피 의무가 없어 종료"),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        job_related_declaration = ft.View(
            "/job_related_declaration",
            [
                ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("직무관련자와의 거래가 신고 조치가 필요합니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
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

        ###
        #
        ###

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
                    on_click=lambda _: page.go("/"),
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
                    on_click=lambda _: page.go("/"),
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
                    on_click=lambda _: page.go("/"),
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
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.Text("퇴직자 사적접촉 신고·회피 의무가 없습니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )

        retired_declaration = ft.View(
            "/retired_declaration",
            [
                ft.AppBar(title=ft.Text("신고조치 필요"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("퇴직자 사적 접촉 신고 조치가 필요합니다."),
                ft.FilledButton(
                    "처음으로",
                    width=500,
                    on_click=lambda _: page.go("/"),
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

        routes = {
            "/": home,
        }
        routes.update(preesent_routes)
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


ft.app(target=main)
# %%
