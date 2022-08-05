# Wartales_KR
Shiro games의 게임 Wartales를 번역하는 프로젝트입니다.

## 번역하기
번역해야하는 파일은 trans 폴더에 있는 export_zh.xml, texts_zh.xml 파일입니다.\
번역은 다음의 2가지 방법으로 가능합니다.
- fork 후 pull request
- collaborator 신청 후 branch에 번역 후 pull request

기본적으로는 fork 후에 PR로 번역하는 것을 권장합니다.\
한번 이상 PR을 생성 한 이후에 다음 discord에서 collaborator 신청을 해주시기 바랍니다.\
[Discord Link](https://discord.gg/Pd3sD9Np7C)\
\
번역 가이드 문서가 만들어 졌습니다.\
다음 링크의 노션 문서를 참조해주세요.\
[Translation Guide Docs](https://elated-dosa-80f.notion.site/Wartales-translation-1ccaf2ddc4bd495bb720de6d944f2364)

## res.pak repack 하기
다음의 순서를 따라서 진행하기 바랍니다.
1. 게임폴더에 있는 `res.pak` 복사 후 리포지토리 루트경로에 붙여넣기
2. `res_repack.bat` 실행
3. 리포지토리 루트에 있는 `res.pak` 복사 후 게임폴더에 붙여넣기

## content.pak repack 하기
다음의 순서를 따라서 진행하기 바랍니다.\
다만, 이전에 생성한 폰트가 존재 한다면 3번부터 진행해도 무방합니다.
1. `fontgen.bat` 실행
2. `fontgen/output` 경로에 `.fnt` `.png` 파일 생성을 확인하기
4. 게임폴더에 있는 `content.pak` 복사 후 리포지토리 루트경로에 붙여넣기
5. `content_repack.bat`을 실행하기
6. 리포지토리 루트에 있는 `content.pak` 복사 후 게임플더에 붙여넣기
