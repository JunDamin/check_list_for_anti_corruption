import flet as ft


def lecture_check(page):

    lecture_intro1 = ft.View(
        "/lecture_intro1",
        [
            ft.AppBar(
                title=ft.Text("체크리스트 목적 및 대상범위 안내"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Markdown("""동 체크리스트는 청탁금지법 제10조, 시행령 제25조 및 제26조에 따른 "외부강의등"에 해당하는지 여부와 E-HR 신고 유형 및 절차를 안내하기 위해 제작되었습니다.
청탁금지법 제8조에 따른 금품등 수수금지, 이해충돌방지법 제10조에 따른 직무 관련 외부활동 제한 등 "외부강의등" 외 사안에 관한 상세 문의는 윤리준법팀으로, 겸직 해당 여부 및 관련 절차에 관한 상세 문의는 인사지원팀으로 별도 문의하시기 바랍니다.
동 체크리스트는 청탁금지법 및 시행령 관련 조문, 국민권익위원회 청탁금지법 해설집, 협력단 임직원 윤리실천규정 관련 조문의 일반적인 내용에 한정하여 제작되었으므로, 사안별 구체적인 사실관계에 따라 해석이 달라질 수 있음을 양지하여 주시기 바랍니다.
                        """),
            ft.ElevatedButton(
                "시작",
                width=500,
                on_click=lambda _: page.go("/lecture_intro2"),
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

    lecture_intro2 = ft.View(
        "/lecture_intro2",
        [
            ft.AppBar(
                title=ft.Text("체크리스트 목적 및 대상범위 안내"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Markdown("""## 신고하시려는 활동이 아래 청탁금지법상 "외부강의등"에 해당합니까?
- 청탁금지법상 "외부강의등": 자신의 직무와 관련되거나 그 지위ㆍ직책 등에서 유래되는 사실상의 영향력을 통하여 요청받은 교육ㆍ홍보ㆍ토론회ㆍ세미나ㆍ공청회 또는 그 밖의 회의 등에서 한 강의ㆍ강연ㆍ
기고 등"""),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),
            ),
            ft.ElevatedButton(
                "모르겠다",
                width=500,
                on_click=lambda _: page.go("/lecture_check1_a"),
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

    lecture_ok = ft.View(
        "/lecture_ok",
        [
            ft.AppBar(
                title=ft.Text("신고 불요"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Markdown("## 외부강의 미해당으로 신고 할 필요가 없습니다."),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    lecture_ok_external = ft.View(
        "/lecture_ok_external",
        [
            ft.AppBar(
                title=ft.Text("신고 불요"),
                bgcolor=ft.colors.GREEN,
            ),
            ft.Markdown('## 청탁금지법상 "외부강의등"에 해당하나 신고 의무가 없고, 대체근무도 불요하므로 E-HR상 부재 신고 불요합니다. 이해충돌 여부 등 타법령 위반이 의심될 경우 윤리준법팀으로 별도 문의하시기 바랍니다.'),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    lecture_ok_declare_internal = ft.View(
        "/lecture_ok_declare_internal",
        [
            ft.AppBar(
                title=ft.Text("신고 의무 발생"),
                bgcolor=ft.colors.RED,
            ),
            ft.Markdown('##  청탁금지법상 "외부강의등"에는 해당하지 않으나, 대체근무를 위해 복무관리상 E-HR 신고가 필요하므로 "외부행사,강의,회의등" 부재 유형에서 청탁금지법 적용 체크란 해제 후 신고 바랍니다.'),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    lecture_ok_declare_external = ft.View(
        "/lecture_ok_declare_external",
        [
            ft.AppBar(
                title=ft.Text("신고 의무 발생"),
                bgcolor=ft.colors.RED,
            ),
            ft.Markdown('##   청탁금지법상 "외부강의등"으로 신고 의무가 없으나, 대체근무를 위해 복무관리상 E-HR 신고가 필요하므로 "외부행사,강의,회의등" 부재 유형에서 청탁금지법 적용 체크란 해제 후 신고 바랍니다.'),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    lecture_declare_internal = ft.View(
        "/lecture_declare_internal",
        [
            ft.AppBar(
                title=ft.Text("신고 의무 발생"),
                bgcolor=ft.colors.RED,
            ),
            ft.Markdown('##  내부강의에 해당하므로 E-hr 부재유형 "내부강의"로 신고하십시오.'),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    lecture_declare_external = ft.View(
        "/lecture_declare_external",
        [
            ft.AppBar(
                title=ft.Text("신고 의무 발생"),
                bgcolor=ft.colors.RED,
            ),
            ft.Markdown('## 청탁금지법의 적용을 받는 "외부강의등"에 해당합니다. E-HR 부재신고 "외부행사,강의,회의등"으로 신고 바랍니다(요청 공문 필첨).'),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )


    lecture_concurrent = ft.View(
        "/lecture_concurrent",
        [
            ft.AppBar(
                title=ft.Text("겸직신고 필요"),
                bgcolor=ft.colors.RED,
            ),
            ft.Markdown("## 인사실을 통해 사전겸직 승인 필요하므로 「임직원 겸직허가 가이드라인」 에서 겸직 승인 절차 확인 또는 인사지원팀 문의"),
            ft.FilledButton(
                "처음으로",
                width=500,
                on_click=lambda _: page.go("/internal"),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.HIDDEN,
    )

    lecture_check1_a = ft.View(
        "/lecture_check1_a",
        [
            ft.AppBar(
                title=ft.Text("1. 외부강의등 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("""# 가. 요청기관의 내/외부 판단
## 요청기관이 어디인가요?
* 요청기관의 내/외부 판단이 어려운 경우, 아래 외부강의 질의회신집(p.11) QnA 참고
Q 외부강의와 내부강의가 헷갈립니다. 어떻게 구분하나요? 
A 일차적으로 요청공문(요청공문 발송기관이 외부기관인지 여부)에 근거하여 판단하며, ODA교육원 및 월드프렌즈본부에서 요청하는 일부 강의를 제외하고는 대부분 외부강의로 구분됩니다. 대학교·국제협력센터 강의 요청 및 사업 프로젝트 내 용역사 등 파트너 기관에 의한 강의 요청은 모두 외부강의에 해당합니다. 예를 들어, ODA 교육원 및 연수사업실 소관 교육 및 연수 사업의 수행을 위탁받은 용역사 등 파트너기관에서 요청한 강의는 외부강의로 분류되며, 외부 요청기관의 공문과 함께 강의 실시내역을 신고해야 합니다. 명확한 내·외부 강의에 대한 판단이 어려울 경우에는 강의 소관부서(ODA교육원 등)에 문의 후, 출강하기 바랍니다.
                        """, width=500),
            ft.ElevatedButton(
                "외부",
                width=500,
                on_click=lambda _: page.go("/lecture_check1_b"),
            ),
            ft.ElevatedButton(
                "내부", width=500, on_click=lambda _: page.go("/lecture_declare_internal")
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

    lecture_check1_b = ft.View(
        "/lecture_check1_b",
        [
            ft.AppBar(
                title=ft.Text("1. 외부강의등 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("""# 나. 직무유관성 판단
## 직무와 관련이 있나요?

- 직무 유관
    - 소속부서 또는 담당업무와 관련이 있는 경우(예: 윤리준법부서 소속 청렴업무 
담당자의 청렴교육 등)
    - 소속부서 또는 담당업무 외 우리 기관 업무 관련(예: ODA, 국제개발협력, KOICA사업 소개 등)                    
- 직무 무관
    - 우리기관 업무와 무관한 경우(예: 인문학, 재테크 강의 등)
                        """, width=500),
            ft.ElevatedButton(
                "직무 유관",
                width=500,
                on_click=lambda _: page.go("/lecture_check3"),
            ),
            ft.ElevatedButton(
                "직무 무관",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_a")
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

    lecture_check1_c = ft.View(
        "/lecture_check1_c",
        [
            ft.AppBar(
                title=ft.Text("1. 외부강의등 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 얼마나 연속해서 진행하나요?", width=500),
            ft.ElevatedButton(
                "장기(겸임교수•시간강사 위촉 또는 1개월을 초과하여 지속적으로 출강하는 경우)",
                width=500,
                on_click=lambda _: page.go("/lecture_concurrent"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "월3회 이하",
                width=500,
                on_click=lambda _: page.go("/lecture_check1_d"),
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_b")
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

    lecture_check1_d = ft.View(
        "/lecture_check1_d",
        [
            ft.AppBar(
                title=ft.Text("1. 외부강의등 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 어떤 활동인가요?", width=500),
            ft.ElevatedButton(
                "강연/강의/회의",
                width=500,
                on_click=lambda _: page.go("/lecture_check1_d_1"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "기고",
                width=500,
                on_click=lambda _: page.go("lecture_check1_d_2"),
            ),
            ft.ElevatedButton(
                "기타",
                width=500,
                on_click=lambda _: page.go("/lecture_check1_d_3"),
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_c")
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

    lecture_check1_d_1 = ft.View(
        "/lecture_check1_d_1",
        [
            ft.AppBar(
                title=ft.Text("1. 외부 강의 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 어떤 활동인가요?", width=500),
            ft.ElevatedButton(
                "다수인을 대상으로 하거나 회의형태인 강의∙강연",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "다수인을 대상으로 하거나 회의형태인 발표∙토론∙심사∙평가∙의결 등",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "회의형태로 이루어지는 자문회의 참석",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "공청회, 간담회 등의 회의에서 사회자 등의 역할을 맡아 회의 진행",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "온라인 동영상 강의",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "소속 기관장의 사전 겸직허가를 받고 학교에 출강",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "각종 법령에 의한 위원회에 참석",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "회의형태가 아닌 면접, 서면심사, 서면 자문 등",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "시험출제위원으로서 시험출제 회의참석",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_d")
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


    lecture_check1_d_2 = ft.View(
        "/lecture_check1_d_2",
        [
            ft.AppBar(
                title=ft.Text("1. 외부 강의 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 어떤 활동인가요?", width=500),
            ft.ElevatedButton(
                "방송 다큐멘터리 등 원고 작성",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "시험출제위원으로서 시험문제 출제",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "잡지∙저널 등 기사, 원고 게재 요청에 따른 기고",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "잡지∙저널 등 요청 없이 공모∙심사에 의해 실시하는 논문 게재",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_d")
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


    lecture_check1_d_3 = ft.View(
        "/lecture_check1_d_3",
        [
            ft.AppBar(
                title=ft.Text("1. 외부 강의 해당여부"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 어떤 활동인가요?", width=500),
            ft.ElevatedButton(
                "언론 인터뷰, 스포츠 해설, 방송 예능 프로그램 등 출연",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "연주회 또는 전시회에서의 연주∙공연 또는 전시",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.ElevatedButton(
                "회의 형태가 아닌 용역∙자문",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a"),  # 종료 후 인사실 문의
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_d")
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

    lecture_check2_a = ft.View(
        "/lecture_check2_a",
        [
            ft.AppBar(
                title=ft.Text("2. 외부강의등 신고 의무"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("""## 가. 외부강의등 실시의 대가로서 사례금 수령하나요?
* 사례금 외에 다른 대가를 받는 경우는 윤리준법팀으로 별도 문의 요망""", width=500),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_check2_b"),  
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_check32_a"),  
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check1_d")
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


    lecture_check2_b = ft.View(
        "/lecture_check2_b",
        [
            ft.AppBar(
                title=ft.Text("2. 외부강의 등 신고 의무"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("""## 나. 외부강의등 요청기관이 "국가 및 지방자치단체"에 해당하나요?

###  외부강의등 신고대상에서 제외되는 ‘국가 및 지방자치단체’의 범위(외부강의 질의회신집 p.8)
                        
- 국회, 법원, 헌법재판소, 선거관리위원회, 감사원, 고위공직자범죄수사처, 국가인권위원회, 「정부조직법」에 따른 중앙행정기관 및 그 소속기관 등의 국가기관
- 국립 유치원, 국립 초･중･고등학교, 국립대학교의 경우 중앙행정기관 중 교육부 소속으로 이에 해당
- 지방자치단체 및 교육청 
- 공립 유치원, 공립 초･중･고등학교, 공립대학교는 교육청, 지방자치단체 소속으로 이에 해당""", width=500),
            ft.ElevatedButton(
                "해당하지 않음",
                width=500,
                on_click=lambda _: page.go("/lecture_declare_external"),  # 외부강의 신고대상 여부 확인
            ),
            ft.ElevatedButton(
                "해당함",
                width=500,
                on_click=lambda _: page.go("/lecture_check32_a"),  # 종료 후 인사실 문의
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check2_a")
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

    lecture_check31_a = ft.View(
        "/lecture_check31_a",
        [
            ft.AppBar(
                title=ft.Text("3.1. (외부강의등 미해당) 대체근무 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("""## 가. 청탁금지법상 "외부강의등"에는 해당하지 않으나, 요청기관으로부터 아래 1)~2)에 해당하는 "금품등"을 수수하였습니까?
                        
1) 금전, 유가증권, 부동산, 물품, 숙박권, 회원권, 입장권, 할인권, 초대권, 관람권, 부동산 등의 사용권 등 일체의 재산적 이익
2) 음식물ㆍ주류ㆍ골프 등의 접대ㆍ향응 또는 교통ㆍ숙박 등의 편의 제공
3) 채무 면제, 취업 제공, 이권(利權) 부여 등 그 밖의 유형ㆍ무형의 경제적 이익
                        """, width=500),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_a_1"),  # 외부강의 신고대상 여부 확인
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_b"),  # 청탕금지법 제 8조?
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check4")
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

    lecture_check31_a_1 = ft.View(
        "/lecture_check31_a_1",
        [
            ft.AppBar(
                title=ft.Text("3.1. (외부강의등 미해당) 대체근무 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("""## 공직자등은 동일인으로부터 1회 100만원 또는 매 회계연도 300만원을 초과하는 금품등을 제공받을 수 없고, 직무와 관련하여는 대가성 여부를 불문하고 금품등을 제공받을 수 없습니다(청탁금지법 제8조제1항, 제2항 참고). 법령 위반이 의심될 경우 윤리준법팀으로 별도 문의하시기 바랍니다.
                        """, width=500),
            ft.ElevatedButton(
                "확인",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_b"),  # 외부강의 신고대상 여부 확인
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check31_a")
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
    
    lecture_check31_b = ft.View(
        "/lecture_check31_b",
        [
            ft.AppBar(
                title=ft.Text("3.1. (외부강의등 미해당) 대체근무 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 나. (서면/대면 여부 무관하게) 근무시간 내 진행되었나요?", width=500),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_check31_c"),  # 외부강의 신고대상 여부 확인
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_ok"),  # 청탕금지법 제 8조?
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check31_a")
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

   
    lecture_check31_c = ft.View(
        "/lecture_check31_c",
        [
            ft.AppBar(
                title=ft.Text("3.1. (외부강의등 미해당) 대체근무 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 다. 개인연차를 사용하였나요?", width=500),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_ok"),  # 외부강의 신고대상 여부 확인
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_ok_declare_internal"),  # 청탕금지법 제 8조?
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check31_b")
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

    lecture_check32_a = ft.View(
        "/lecture_check32_a",
        [
            ft.AppBar(
                title=ft.Text("3.2. (외부강의등 해당하나, 신고의무 없음) 대체근무 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 가. (서면 여부, 대면 여부 무관하게) 근무시간 내 진행되었나요?", width=500),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_check32_b"),  # 외부강의 신고대상 여부 확인
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_ok_external"),  # 청탕금지법 제 8조?
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check2_a")
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

    
    lecture_check32_b = ft.View(
        "/lecture_check32_b",
        [
            ft.AppBar(
                title=ft.Text("3.2. (외부강의등 해당하나, 신고의무 없음) 대체근무 판단"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
            ft.Markdown("## 개인연차를 사용하였나요?", width=500),
            ft.ElevatedButton(
                "예",
                width=500,
                on_click=lambda _: page.go("/lecture_ok_external"),  # 외부강의 신고대상 여부 확인
            ),
            ft.ElevatedButton(
                "아니오",
                width=500,
                on_click=lambda _: page.go("/lecture_ok_declare_external"),  # 청탕금지법 제 8조?
            ),
            ft.FilledButton(
                "뒤로", width=500, on_click=lambda _: page.go("/lecture_check32_a")
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




    lecture_routes = {
        "/lecture_intro1": lecture_intro1,
        "/lecture_intro2": lecture_intro2,
        "/lecture_ok": lecture_ok,
        "/lecture_ok_external": lecture_ok_external,
        "/lecture_ok_declare_internal": lecture_ok_declare_internal,
        "/lecture_declare_internal": lecture_declare_internal,
        "/lecture_declare_external": lecture_declare_external,
        "/lecture_ok_declare_external": lecture_ok_declare_external,
        "/lecture_concurrent": lecture_concurrent,
        "/lecture_check1_a": lecture_check1_a,
        "/lecture_check1_b": lecture_check1_b,
        "/lecture_check1_c": lecture_check1_c,
        "/lecture_check1_d": lecture_check1_d,
        "/lecture_check1_d_1": lecture_check1_d_1,
        "/lecture_check1_d_2": lecture_check1_d_2,
        "/lecture_check1_d_3": lecture_check1_d_3,
        "/lecture_check2_a": lecture_check2_a,
        "/lecture_check2_b": lecture_check2_b,
        "/lecture_check31_a": lecture_check31_a,
        "/lecture_check31_a_1": lecture_check31_a_1,
        "/lecture_check31_b": lecture_check31_b,
        "/lecture_check31_c": lecture_check31_c,
        "/lecture_check32_a": lecture_check32_a,
        "/lecture_check32_b": lecture_check32_b,
    }

    return lecture_routes


if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "반부패 이해충돌 방지 자가진단 체크리스트"

        def route_change(route):
            page.views.clear()

            routes = {}
            lecture_routes = lecture_check(page)
            routes.update(lecture_routes)

            page.views.append(
                routes.get(page.route, lecture_check(page).get("/lecture_check1"))
            )

            page.update()

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
