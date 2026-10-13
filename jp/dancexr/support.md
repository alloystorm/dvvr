---
layout: studio-home
title: サポート
toc: false
locale: ja-JP
lang_path: /dancexr/support
hero_compact: true
hero_title: サポート
hero_image: /images/hero.png
support_categories:
  - id: "content"
    label: "コンテンツと設定"
  - id: "actors"
    label: "アクターと外観"
  - id: "motion"
    label: "モーションと再生"
  - id: "environment"
    label: "環境と照明"
  - id: "camera"
    label: "カメラと録画"
  - id: "saving"
    label: "保存と共有"
  - id: "vr"
    label: "VRとデバイス"
  - id: "help"
    label: "トラブルシューティングとライセンス"
support_sections:
  - id: "how-to"
    label: "操作ガイド"
    title: "操作方法"
    subsections:
      - title: "コンテンツと設定"
        items:
          - id: "find-content-library"
            category: "content"
            type: "how-to"
            question: "コンテンツライブラリはどこにありますか？"
            keywords: ["content library", "folder", "Explorer", "storage", "コンテンツライブラリ", "フォルダー", "保存場所", "ストレージ"]
            related: [{"href": "preparecontent", "label": "コンテンツライブラリ"}]
            answer: "Windowsでは、**システム**メニュー（歯車アイコン）から **コンテンツライブラリ → エクスプローラーで表示** を選ぶと、ライブラリのフォルダーを開けます。\n\nAndroidとMeta Questの共有ライブラリは通常 `/DanceXR/` にあります。古いバージョンや内部ストレージを使う場合は `/Android/data/com.vrstormlab.dancexr/files/` です。iPhoneやiPadでは、ファイルアプリの **このiPhone内** または **このiPad内** にあるDanceXRフォルダーを開いてください。"
          - id: "add-models"
            category: "content"
            type: "how-to"
            question: "自分のモデルを追加するにはどうすればよいですか？"
            keywords: ["import model", "PMX", "XPS", "FBX", "ZIP", "drag and drop", "モデル追加", "モデル読み込み", "ドラッグ＆ドロップ", "テクスチャ"]
            related: [{"href": "getting-started", "label": "はじめに"}]
            answer: "モデルとテクスチャを、元のフォルダー構成を保ったままコンテンツライブラリの `actors/` にコピーします。モデル一式を個別のZIPファイルにまとめても構いません。\n\n**アクター**メニューで **モデルを読み込む** を選び、モデルを選択します。デスクトップでは、モデルファイルやモデルのZIPをDanceXRのウィンドウにドラッグ＆ドロップすることもできます。\n\nPMXとXPSに対応しています。FBXモデルの読み込みはプレビュー機能で、FBXに埋め込まれたアニメーションは読み込まれません。"
          - id: "add-motions-and-music"
            category: "content"
            type: "how-to"
            question: "モーションと音楽を追加するにはどうすればよいですか？"
            keywords: ["VMD", "BVH", "audio", "music", "WAV", "OGG", "load motion", "モーション追加", "音楽追加", "音声", "ダンスセット"]
            related: [{"href": "preparecontent#motion-files", "label": "コンテンツライブラリ"}]
            answer: "VMDまたはBVHのモーションファイルと音声ファイルを、コンテンツライブラリの `motion/` に入れます。ダンスセットにはWAVまたはOGGの音声を使えます。\n\n**音声／モーション**メニューの **音声／モーションを読み込む** から選択します。デスクトップでは、ファイルをDanceXRのウィンドウへドラッグ＆ドロップすることもできます。\n\n音楽とモーションをまとめて読み込むには、1曲の音声と関連するモーションを同じサブフォルダーまたはZIPに入れてください。モーションと音声が1組だけなら、`dance.vmd` と `dance.ogg` のように名前を揃える方法も使えます。"
          - id: "refresh-content-library"
            category: "content"
            type: "how-to"
            question: "追加したファイルをライブラリに表示するにはどうすればよいですか？"
            keywords: ["refresh", "rescan", "missing files", "new content", "ライブラリ更新", "再スキャン", "ファイルが表示されない", "新しいコンテンツ"]
            related: [{"href": "preparecontent", "label": "コンテンツライブラリ"}]
            answer: "**システム → コンテンツライブラリ → コンテンツを更新** を選び、スキャンが完了するまで待ちます。DanceXRの起動中にファイルをコピーしたり移動したりした後に使ってください。\n\n起動時にもライブラリの変更を確認します。表示されない場合は、保存先のサブフォルダーを確認してください。モデルは `actors/`、モーションと音声は `motion/`、ステージは `stages/`、スカイマップは `texture/sky/` です。"
      - title: "アクターと外観"
        items:
          - id: "add-another-actor"
            category: "actors"
            type: "how-to"
            question: "現在のアクターを置き換えずに別のアクターを追加するには？"
            keywords: ["multiple actors", "add character", "replace model", "plus", "アクター追加", "複数のモデル", "モデル置き換え", "有料版"]
            related: [{"href": "getting-started", "label": "はじめに"}]
            answer: "**アクター → モデルを読み込む** を開き、追加したいモデルの横にある **+** アイコンをクリックします。通常のモデル選択では現在選択中のアクターを置き換えますが、+を使うと元のアクターを残して追加できます。\n\n複数のアクターを使うには、有料版のアクティベーションが必要です。+が使えない場合は、エディションとライセンスの有効化状況を確認してください。"
          - id: "move-and-rotate-actor"
            category: "actors"
            type: "how-to"
            question: "アクターを移動・回転・拡大縮小するには？"
            keywords: ["scale", "resize", "position", "move", "rotate", "selection disc", "移動", "回転", "拡大縮小", "サイズ変更", "選択ディスク"]
            related: [{"href": "actors", "label": "アクターの操作"}, {"href": "features/scale_offset", "label": "スケールとオフセット"}, {"href": "controls", "label": "操作とUI"}]
            answer: "アクターの足元にある黄色い選択ディスクをドラッグすると移動できます。ドラッグ中にマウスホイールを使うと回転します。VRではコントローラーのスティックを左右に動かしてください。\n\n細かく調整するには、アクターの **スケールとオフセット** を開きます。**モデルスケール** で大きさ、**回転** で向き、**オフセットX/Z** で水平位置、**地面オフセット** で高さを調整します。モデル本来の大きさを保ちたい場合は **身長を統一** をオフにしてください。"
          - id: "change-model-textures"
            category: "actors"
            type: "how-to"
            question: "モデルのテクスチャを変更するには？"
            keywords: ["alternative textures", "replace texture", "skin", "base.png", "テクスチャ変更", "代替テクスチャ", "差し替え", "モデルの見た目"]
            related: [{"href": "features/alternative_textures", "label": "代替テクスチャ"}]
            answer: "代替テクスチャは、モデルのフォルダー内の別のサブフォルダー、または同じモデルZIP内に配置します。差し替えるテクスチャと同じファイル名にしてください。\n\n例えば、モデルが `base.png` を使っている場合は、`alternate/` サブフォルダーに別の `base.png` を入れます。モデルを再読み込みし、アクターメニューの **代替テクスチャ** でDanceXRが検出したセットを選択してください。スキャンできるよう、代替ファイルもモデルのパッケージ内に置く必要があります。"
          - id: "attach-hand-prop"
            category: "actors"
            type: "how-to"
            question: "アクターの手に小道具を持たせるには？"
            keywords: ["accessory", "prop", "hand", "grab pose", "attachment", "小道具", "手に持たせる", "アクセサリー", "取り付け", "握りポーズ"]
            related: [{"href": "features/accessory", "label": "アクセサリー"}]
            answer: "小道具のモデルとテクスチャをコンテンツライブラリの `accessory/` に入れ、必要に応じてライブラリを更新します。\n\nアクターを選択して **アクセサリー** を開きます。**左手** または **右手** を有効にし、**モデル** で小道具を選択してください。**サイズと位置合わせ**、**回転**、**オフセット** を調整して手に合わせます。対応している場合は **握りポーズ** で握り方も調整できます。\n\nアクセサリー機能を利用できるエディションが必要です。"
      - title: "モーションと再生"
        items:
          - id: "assign-motion"
            category: "motion"
            type: "how-to"
            question: "アクターにモーションを割り当てるには？"
            keywords: ["assign motion", "animation", "selected actor", "dance", "モーション割り当て", "アニメーション", "選択したアクター", "ダンス"]
            related: [{"href": "features/assign_motion", "label": "モーションの割り当て"}]
            answer: "**音声／モーション**メニューでモーションを読み込み、動かしたいアクターを選択します。\n\nモーションを選び、**選択したアクターに割り当て** を使います。アクターメニューのモーション一覧から、読み込んだモーションを選ぶこともできます。全員に同じ動きをさせる場合は **すべてに割り当て** を使ってください。\n\nXPSやFBXのアクターが標準ポーズのまま動かない場合は、**ボーンマッパー** の割り当てを確認してください。"
          - id: "assign-group-dance"
            category: "motion"
            type: "how-to"
            question: "複数のアクターに別々のダンストラックを割り当てるには？"
            keywords: ["group dance", "multiple tracks", "assign all actors", "グループダンス", "複数のトラック", "全員に割り当て", "自動割り当て"]
            related: [{"href": "features/assign_motion", "label": "モーションの割り当て"}]
            answer: "グループダンスのセットを読み込み、すべてのモーショントラックを使える状態にします。モーションメニューの **すべてのアクターに割り当て** を使うと、シーン内のアクターに別々のトラックを割り当てられます。\n\nアクターの読み込みも自動で行いたい場合は **アクターを読み込んで割り当て** を使います。手動で決める場合は、アクターを1人ずつ選び、使いたいトラックの **選択したアクターに割り当て** を選択してください。\n\n複数のアクターを使うには、有料版のアクティベーションが必要です。"
          - id: "organize-dance-set"
            category: "motion"
            type: "how-to"
            question: "音楽・アクターのモーション・カメラモーションをダンスセットにまとめるには？"
            keywords: ["dance set", "package", "group music", "camera VMD", "ZIP", "ダンスセット", "音楽とモーション", "まとめる", "カメラモーション"]
            related: [{"href": "preparecontent#motion-files", "label": "コンテンツライブラリ"}]
            answer: "`motion/` の中にサブフォルダーまたはZIPを作り、曲、アクターのモーションファイル、カメラモーションを入れます。音声ファイルは1つだけにしてください。DanceXRが関連ファイルをダンスセットとして認識し、まとめて読み込めるようになります。\n\nモーションと音声が1組だけなら、`dance.vmd` と `dance.ogg` のようにファイル名を揃えても認識されます。無関係なファイルが同じフォルダーにある場合は、別々のパッケージに分けてください。"
          - id: "map-xps-fbx-bones"
            category: "motion"
            type: "how-to"
            question: "XPSやFBXモデルをモーションで動かすには？"
            keywords: ["bone mapping", "XPS", "FBX", "T-pose", "Auto Map", "Chain Mapping", "ボーンマッピング", "標準ポーズのまま", "自動マッピング", "チェーンマッピング"]
            related: [{"href": "features/bone_mapper", "label": "ボーンマッパー"}]
            answer: "モデルを読み込み、アクターメニューの **ボーンマッパー** を開きます。**自動マッピング** を実行し、感嘆符が付いたスロットを確認してください。動作に必要なボーンがまだ割り当てられていないことを示します。\n\n未割り当てのスロットに、モデルの対応するボーンを指定します。**チェーンマッピング** を使うと腕や手などのボーン列を素早く設定できます。必須ボーンの設定が終わったら、モーションを割り当てて確認してください。\n\nXPSとFBXにはボーンマッピングが必要です。PMXは通常、標準のボーン名を持っています。"
      - title: "環境と照明"
        items:
          - id: "change-sky-map"
            category: "environment"
            type: "how-to"
            question: "自分のスカイマップやHDRI背景を使うには？"
            keywords: ["HDRI", "skybox", "panorama", "background", "environment map", "空の背景", "スカイマップ", "環境マップ", "パノラマ", "背景変更"]
            related: [{"href": "features/sky", "label": "空"}, {"href": "preparecontent", "label": "コンテンツライブラリ"}]
            answer: "パノラマの空画像を、コンテンツライブラリの `texture/sky/` に入れます。環境マップにはHDR形式をおすすめします。起動中に追加した場合は **システム → コンテンツライブラリ → コンテンツを更新** を使ってください。\n\n**環境 → 空** を開き、**モード** を **スカイマップ** にして、**スカイマップ** から画像を選択します。背景を回転させるには **向き** を調整してください。"
          - id: "rotate-sky-map"
            category: "environment"
            type: "how-to"
            question: "空の背景を回転させるには？"
            keywords: ["sky orientation", "rotate panorama", "skybox", "空の回転", "背景の向き", "パノラマ回転", "スカイマップ"]
            related: [{"href": "features/sky", "label": "空"}, {"href": "features/sky", "label": "空"}]
            answer: "**環境 → 空** を開き、**モード** が **スカイマップ** になっていることを確認します。**向き** を調整すると、パノラマがシーンの周囲を回転します。\n\n地面のスカイドーム材質に使う空の投影も回転するため、変更後は地面と反射も確認してください。"
          - id: "adjust-sky-lighting"
            category: "environment"
            type: "how-to"
            question: "空の明るさと環境光を別々に調整するには？"
            keywords: ["ambient lighting", "sky exposure", "brightness", "washed out", "空の明るさ", "環境光", "露出", "白飛び", "照明"]
            builds: ["HD", "RT", "LW"]
            related: [{"href": "features/sky", "label": "空"}]
            answer: "**環境 → 空** を開きます。\n\nHD/RT版では **背景** が見える空の明るさ、**スカイアンビエント** がシーンへの環境光の寄与を制御します。明るい背景でアクターの陰影が薄くなる場合は、スカイアンビエントを下げてください。\n\n軽量版では **スカイエクスポージャー** と **強度** を使います。スカイエクスポージャーは反射の明るさにも影響するため、反射する材質も確認しながら調整してください。"
          - id: "load-stage"
            category: "environment"
            type: "how-to"
            question: "自分のステージを読み込むには？"
            keywords: ["stage", "environment model", "Load Stage", "stages folder", "ステージ読み込み", "舞台", "ステージタグ", "小道具のアニメーション"]
            related: [{"href": "features/stages", "label": "ステージ"}]
            answer: "ステージモデルと必要なテクスチャを、元のフォルダー構成のままコンテンツライブラリの `stages/` に入れるか、一式をZIPにまとめます。**stage** タグを付けたアクターモデルもステージメニューに表示できます。\n\n必要に応じてライブラリを更新し、**シーン → ステージを読み込む** から選択します。新しいステージを読み込むと前のステージを置き換えます。読み込んだステージの設定で見た目や配置を調整してください。\n\nステージや小道具として読み込んだモデルはモーションを再生できません。動かす場合はファイルを `actors/` に置き、アクターとして読み込んでモーションを割り当てます。スカイマップは別のもので、`texture/sky/` に入れます。"
      - title: "カメラと録画"
        items:
          - id: "hide-ui"
            category: "camera"
            type: "how-to"
            question: "メニューやアクターの操作表示を隠すには？"
            keywords: ["hide UI", "immersive mode", "menus", "selection discs", "Esc", "UIを隠す", "メニュー非表示", "没入モード", "選択ディスク"]
            related: [{"href": "controls", "label": "操作とUI"}]
            answer: "何もない場所をクリックすると、**UI**、**操作**、**没入**モードを順に切り替えます。没入モードでは、メニューと黄色いアクター選択ディスクの両方を隠せます。\n\n割り当て済みの **UI切り替え** 操作も使えます。デスクトップの初期設定は **Esc** です。何もない場所をクリックするか、もう一度UI切り替えを使うと表示を戻せます。"
          - id: "use-camera-motion"
            category: "camera"
            type: "how-to"
            question: "ダンスに付属するカメラモーションを使うには？"
            keywords: ["camera VMD", "camera motion", "dance camera", "imported camera", "カメラモーション", "カメラVMD", "ダンスのカメラ", "カメラトラック"]
            related: [{"href": "cameras", "label": "シネマティックカメラ"}, {"href": "features/assign_motion", "label": "モーションの割り当て"}, {"href": "preparecontent#motion-files", "label": "コンテンツライブラリ"}]
            answer: "カメラVMDを、曲やアクターのモーションと同じダンスセットのフォルダーまたはZIPに入れ、そのセットを読み込みます。\n\n**カメラ** を開き、読み込んだセットのカメラモーションを選択します。FreeflyやAutoなどの内蔵カメラモードは別の選択肢です。ダンス用に作られたカメラの動きを使うには、読み込んだトラックを選んでください。\n\nトラックが表示されない場合は、読み込んだパッケージにファイルが含まれているか確認します。VRではデスクトップ表示や録画用のカメラに適用され、ヘッドセットの視点は頭の動きに従います。"
          - id: "record-4k"
            category: "camera"
            type: "how-to"
            question: "滑らかな4K動画を録画するには？"
            keywords: ["4K", "offline rendering", "Creator", "60fps", "recording", "4K録画", "オフラインレンダリング", "フレームレート", "動画出力"]
            editions: ["Creator"]
            related: [{"href": "features/recording_settings", "label": "録画設定"}, {"href": "creator", "label": "Creatorエディション"}]
            answer: "オフラインレンダリングには **Creator Edition** を使います。録画メニュー（赤い丸）から **録画設定** を開き、**UHD 3840x2160**、希望する **フレームレート**、画像形式を選択します。\n\nプレビューで構図とモーションを確認し、**2D** 録画を開始します。実時間の再生がその速度に達しなくても、指定した出力フレームレートで各フレームをレンダリングします。\n\n出力は連番画像です。レンダリング後に動画へ変換してください。手順は連番画像を動画に変換する回答をご覧ください。"
          - id: "frames-to-video"
            category: "camera"
            type: "how-to"
            question: "録画した連番画像を動画にするには？"
            keywords: ["FFmpeg", "image sequence", "frames to video", "MP4", "sound.wav", "連番画像", "画像から動画", "動画変換", "音声", "フレーム"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creatorエディション"}]
            answer: "レンダリングしたフレームのフォルダーを開きます。FFmpegがインストールされ、システムのPATHから使える場合は、録画に付属する変換用バッチファイルを実行できます。連番画像を読み込める動画編集ソフトも使えます。\n\n手動変換の例です。60 fpsで録画した `movie_0000.jpg`、`movie_0001.jpg` などのファイルを想定しています。\n\n```sh\nffmpeg -framerate 60 -i movie_%04d.jpg -i sound.wav movie.mp4\n```\n\nフレームレート、番号の形式、拡張子を実際の出力に合わせてください。音声が不要なら `-i sound.wav` を省きます。"
          - id: "record-without-creator"
            category: "camera"
            type: "how-to"
            question: "Creator Editionなしで動画を録画するには？"
            keywords: ["screen recording", "OBS", "real-time capture", "non-Creator", "portrait", "landscape", "window resolution", "画面録画", "実時間録画", "縦向き", "横向き", "ウィンドウ解像度"]
            platforms: ["Windows", "macOS"]
            related: [{"href": "features/display_settings", "label": "ディスプレイ設定"}, {"href": "controls", "label": "操作とUI"}]
            answer: "画面録画ソフトで、DanceXRの実時間再生を録画できます。Creator Editionは必要ありません。\n\n1. **システム → ディスプレイとUI → 解像度** を開き、**フルスクリーン** をオフにしてウィンドウ表示にします。\n2. **ウィンドウ解像度** を選びます。縦向きは **縦表示** をオン、横向きはオフにします。\n3. **解像度を適用** をクリックし、構図を調整します。すっきりした映像にしたい場合はUIを隠してください。\n4. 録画ソフトでDanceXRのウィンドウと音声を録画対象にし、録画を開始してからモーションを再生します。\n\n録画の滑らかさは実際の再生フレームレートに左右されます。再生がカクつく場合は、画質設定や解像度を下げてください。"
      - title: "保存と共有"
        items:
          - id: "save-scene"
            category: "saving"
            type: "how-to"
            question: "シーンを保存して開き直すには？"
            keywords: ["save scene", "load scene", "restore setup", "シーン保存", "シーン読み込み", "設定の復元", "保存済みシーン"]
            related: [{"href": "features/save_scene", "label": "シーンの保存"}]
            answer: "アクター、ステージ、モーション、環境、カメラを配置したら、**シーン** を開き、保存済みシーンのブラウザーにある保存アイコンを使います。名前を入力して **保存** を選択してください。\n\n開き直すには、シーンブラウザーで保存した名前を選びます。シーンには設定とコンテンツへの参照が保存されるため、元のモデルやモーションをライブラリに残してください。素材も一緒に転送する場合は **シーンバンドル** を使います。"
          - id: "share-scene-bundle"
            category: "saving"
            type: "how-to"
            question: "シーンをモデルやモーションと一緒に別の端末へ移すには？"
            keywords: ["scene bundle", "transfer", "share scene", "ZIP", "assets", "シーンバンドル", "シーン転送", "素材を共有", "別の端末"]
            related: [{"href": "features/scene_bundle", "label": "シーンバンドル"}]
            answer: "**シーンバンドル** を使うと、シーンとモデル、ステージ、小道具、アクセサリー、ダンスセットを一つにまとめられます。\n\nシーンを読み込んで確認し、**シーン → バンドル** の保存操作で名前を付けます。**バンドルを作成中...** が終了したら、アーカイブを転送先のコンテンツライブラリの `bundles/` にコピーして開いてください。\n\n転送先で再生と材質を確認します。利用できる機能は転送先のビルドとエディションによって変わります。バンドルメニューを使うには、有料版のアクティベーションが必要です。"
          - id: "save-actor-preset"
            category: "saving"
            type: "how-to"
            question: "アクターの設定を保存して再利用するには？"
            keywords: ["actor preset", "save actor settings", "global preset", "アクタープリセット", "アクター設定保存", "グローバルプリセット", "再利用"]
            related: [{"href": "features/actor_presets", "label": "アクタープリセット"}]
            answer: "アクターを設定したら **プリセット** を開きます。モデルに紐づける場合は **アクタープリセットを保存**、他のアクターでも使う場合は **グローバルに保存** を選び、名前を付けて保存します。\n\n再利用するには、アクターを選択し、プリセットメニューで保存した項目を選びます。プリセットには設定が保存され、モデルファイルは含まれません。別のモデルに適用する場合は、ボーンマッピング、材質スロット、物理設定の違いを確認してください。"
          - id: "save-environment-preset"
            category: "saving"
            type: "how-to"
            question: "照明や環境の設定を保存して再利用するには？"
            keywords: ["system preset", "save lighting", "environment settings", "システムプリセット", "照明設定保存", "環境設定", "設定再利用"]
            related: [{"href": "features/system_presets", "label": "システムプリセット"}]
            answer: "照明、空、地面などのアプリ設定を調整し、**環境 → システムプリセット** を開きます。保存操作で名前を入力して **保存** を選んでください。\n\n同じメニューで保存済みのプリセットを選ぶと再適用できます。設定はライブラリの `presets/system/` に保存されます。アクター、読み込んだコンテンツ、モーションの割り当ても復元したい場合は、シーンを保存してください。"
      - title: "VRとデバイス"
        items:
          - id: "enable-vr"
            category: "vr"
            type: "how-to"
            question: "DanceXRをVRで使うには？"
            keywords: ["VR", "OpenXR", "headset", "SteamVR", "Meta", "VR起動", "ヘッドセット", "ランタイム", "仮想現実"]
            related: [{"href": "vr_operations", "label": "VRでの操作"}, {"href": "faq", "label": "よくある質問"}]
            answer: "PCではヘッドセットを接続し、VRソフトを起動します。SteamVRやMetaなど、使うランタイムが有効な **OpenXR** ランタイムに設定されていることを確認してください。\n\nVR対応のDanceXRビルドを起動し、**環境** メニューの **VR** を有効にします。Quest単体で使う場合は、ヘッドセットにインストールしたQuest版を起動してください。\n\nVRが起動しない場合は、有効なランタイムを確認し、VR起動のトラブルシューティングをご覧ください。"
          - id: "android-quest-library"
            category: "vr"
            type: "how-to"
            question: "AndroidやMeta Questにコンテンツを追加するには？"
            keywords: ["Android", "Meta Quest", "storage permission", "content library", "Quest", "File Transfer", "storage", "Androidのコンテンツ", "Questのライブラリ", "ファイル転送", "ストレージ権限"]
            related: [{"href": "content_android_quest", "label": "AndroidとQuestのコンテンツライブラリ"}]
            answer: "共有フォルダー `/DanceXR/` を使うため、DanceXRに必要なストレージ権限を許可してください。モデルは `actors/`、モーションと音声は `motion/`、その他は対応するライブラリのサブフォルダーに入れます。\n\n端末のファイルアプリを使うか、USBでPCに接続して **ファイル転送** を選択します。Androidの **コンテンツマネージャー** アプリでも、対応するZIPや画像を追加できます。\n\n古いバージョンや内部ストレージモードでは `/Android/data/com.vrstormlab.dancexr/files/` を使います。コピー後はDanceXRを再起動するか、**コンテンツを更新** を実行してください。"
          - id: "start-mobile-ar"
            category: "vr"
            type: "how-to"
            question: "対応するAndroidやiOS端末でARを開始するには？"
            keywords: ["AR", "augmented reality", "Android", "iOS", "camera", "mobile", "AR開始", "拡張現実", "カメラ背景", "モバイル", "対応端末"]
            platforms: ["Android", "iOS"]
            editions: ["Pro"]
            related: [{"href": "features/ar_mode", "label": "AR設定"}]
            answer: "対応するAndroidまたはiOS端末でDanceXRを起動し、**環境** メニューから **AR** を選択します。カメラへのアクセスを求められたら許可し、ARの初期化が終わるまで待ってください。\n\nAR設定の **カメラを表示** で現実の背景を表示します。アクターを実際の床に立たせるように見せるには **地面を隠す** を有効にしてください。通常モードに戻すには **ARを停止** を使います。\n\nARにはアクティベーション済みのPro版と対応する端末・ビルドが必要です。ARが表示されない場合は、端末の対応状況とライセンスの両方を確認してください。Questのパススルーは別の項目で説明しています。"
      - title: "トラブルシューティングとライセンス"
        items:
          - id: "white-model"
            category: "help"
            type: "troubleshooting"
            question: "真っ白に表示されるモデルを直すには？"
            keywords: ["missing textures", "white model", "ZIP encoding", "jis932", "gb2312", "白いモデル", "テクスチャが見つからない", "文字コード", "ZIPの文字化け"]
            related: [{"href": "features/zip_format", "label": "ZIP形式"}, {"href": "preparecontent", "label": "コンテンツライブラリ"}, {"href": "faq", "label": "よくある質問"}]
            answer: "モデルが真っ白になるのは、通常テクスチャファイルが見つからないためです。モデルファイルを基準とした元の位置にテクスチャを保ってください。\n\n日本語や中国語のファイル名を含むZIPでは、対応する文字コードの接尾辞を試します。日本語なら `model.jis932.zip`、中国語なら `model.gb2312.zip` です。名前を変更したらモデルを再読み込みしてください。Androidのコンテンツマネージャーでも文字コードを設定できます。\n\n改善しない場合は、モデルのテクスチャ参照を調べ、ファイル名、フォルダーのパス、空白が実際のファイルと一致しているか確認してください。"
          - id: "transparent-hair"
            category: "help"
            type: "troubleshooting"
            question: "髪が透けて見える問題を直すには？"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "髪が透ける", "透明度", "深度プリパス", "透明レイヤー", "描画順"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "透明材質"}, {"href": "faq", "label": "よくある質問"}]
            answer: "HD/RT版では、透明度の深度プリパスにより、複数の透明レイヤーを持つ髪の奥側のレイヤーが消えることがあります。\n\n**システム → グラフィックス → オプション → 透明プリパス** をオフにして比較してください。影響を限定するには、問題のある髪の材質だけで透明プリパスを調整します。\n\nオフにすると別の透明度の描画順の問題が現れる場合があります。複数の角度から確認し、そのモデルで最もよい結果になる設定を選んでください。"
          - id: "vr-will-not-start"
            category: "help"
            type: "troubleshooting"
            question: "VRが起動しない場合はどうすればよいですか？"
            keywords: ["OpenXR", "SteamVR", "Oculus", "VR launch", "VR startup", "Meta", "VRが起動しない", "VR起動エラー", "ランタイム", "オーバーレイ"]
            related: [{"href": "troubleshooting", "label": "トラブルシューティング"}, {"href": "faq", "label": "よくある質問"}]
            answer: "VRソフトが起動していて、ヘッドセット用のランタイムが有効な **OpenXR** ランタイムに設定されていることを確認します。複数のランタイムがある場合は、使いたいものの設定で有効にし、ランタイムとDanceXRを再起動してください。\n\n再び **環境 → VR** を有効にします。それでも起動しない場合は、不要なVRオーバーレイやアドオンを無効にし、DanceXRの `Player.log` でエラーを確認します。問題を報告する際は、ログ、アプリのビルド、ヘッドセットとランタイムの情報を添えてください。"
          - id: "reactivate-license"
            category: "help"
            type: "how-to"
            question: "ライセンスを有効化・再有効化するには？"
            keywords: ["activation", "license", "hardware change", "activate", "reactivate", "purchase", "entitlement", "ライセンス有効化", "再アクティベーション", "購入確認", "ライセンス復元"]
            related: [{"href": "activation", "label": "アクティベーションとライセンス"}]
            answer: "Steam版とGoogle Play版は、通常ストアで購入が確認されると自動的に有効化されます。\n\n手動の有効化が必要なエディションでは、**システム → ライセンスを有効化** を開きます。ブラウザーの案内に従い、購入したプラットフォームを選んでログインしてください。成功画面が表示されたらDanceXRに戻り、もう一度 **ライセンスを有効化** をクリックしてライセンスを取得します。\n\nその端末で以前に有効化していれば、ブラウザーを開かずに復元できる場合があります。再インストール、ハードウェア変更、ビルドの切り替え後に再有効化しても、追加料金はかかりません。"
  - id: "faq"
    label: "よくある質問"
    title: "よくある質問（FAQ）"
    subsections:
      - title: "🌐 よくある問題"
        items:
          - id: "stage-sky-holes"
            category: "environment"
            type: "troubleshooting"
            question: "ステージモデルのスカイスフィアに穴が開いている、またはピクセル化して見える"
            keywords: ["sky sphere", "skybox", "pixelated background", "depth prepass"]
            answer: "これも透明度の深度プリパスが原因です。複数のスカイスフィアが透明な場合、一部の領域では最上層のみが完全にレンダリングされます。\n\n- 透明度の深度プリパスをオフにする、または\n- 背景のスカイスフィアを見つけ、そのマテリアルを透明から不透明に変更する。"
      - title: "🛠️ 報告前のチェックリスト"
        items:
          - id: "before-reporting"
            category: "help"
            type: "troubleshooting"
            question: "バグを報告する前に、以下の簡単な修正をお試しください："
            keywords: ["bug report", "reset settings", "cache", "OpenXR"]
            answer: "1. **最新バージョンに更新** — 問題が新しいリリースですでに解決されている可能性があります。\n2. **設定のリセット** — 破損した設定ファイルを排除するために、バックアップを取ってから `config.json` を削除します。\n3. **ライセンスのリセット** — アプリの起動に失敗したり動作がおかしい場合は、インストールディレクトリから `license.txt` を削除して再起動してみてください。\n4. **ライブラリキャッシュのクリア** — コンテンツライブラリフォルダから `cache.json` をバックアップして削除し、プレイヤーにファイルの再スキャンを強制します。\n5. **OpenXRセットアップ** — VRが起動しない場合は、VRソフトウェアの設定でアクティブなOpenXRランタイムが正しく設定されているか再確認してください。"
          - id: "find-log-files"
            category: "help"
            type: "troubleshooting"
            question: "ログファイルはどこにありますか？"
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report"]
            answer: "バグを報告する際、ログファイルを添付すると非常に役立ちます。バグ報告には、**`Player.log`**（現在のセッション）と**`Player-prev.log`**（以前のセッション）を添付してください。\n\n**Windows PCのパス:**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*注: `[User]`をWindowsのユーザー名に置き換えてください。AppDataが隠しフォルダになっている場合は、エクスプローラーで「隠しファイル」を表示する設定にしてください。*\n\n**Android & Meta Questのパス:**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*注: デバイスをUSBでPCに接続し、ファイル転送モードを使用してこのファイルを見つけてください。*"
      - title: "🖥️ システム & VRの起動"
        items:
          - id: "startup-sky-only"
            category: "help"
            type: "troubleshooting"
            question: "空だけが表示され、UIやカメラ操作ができない"
            keywords: ["startup", "no UI", "no controls", "config.json"]
            answer: "これは通常、起動時に何らかの問題が発生していることを意味します。以下の手順を順番にお試しください：\n\n- `license.txt`を削除して再起動する。\n- `config.json`を削除する（先にバックアップすること）—これによりすべての設定がリセットされ、破損した設定ファイルが原因の問題が解決します。\n- コンテンツライブラリから`cache.json`を削除する（先にバックアップすること）。"
          - id: "startup-crash"
            category: "vr"
            type: "troubleshooting"
            question: "起動するたびにクラッシュする—古いバージョンに戻しても改善しない"
            keywords: ["crash", "SteamVR", "runtime", "startup"]
            answer: "これは通常、DanceXR自体ではなく、VRランタイムの問題です。\n\n- 複数のVRランタイムがある場合は、別のものに切り替えてみる。\n- SteamVRの場合：不要な起動オーバーレイやアドオンを無効にし、クリーン再インストールを試してください。\n- SteamVRの`driver`フォルダー内で、削除できる最近インストールまたは更新されたものがないか確認する。"
  - id: "known-issues"
    label: "既知の問題"
    title: "既知の問題と回避策"
    subsections:
      - title: "📌 バージョン 2026.6"
        items:
          - id: "motion-smoothing-2026-6"
            category: "motion"
            type: "known-issue"
            question: "モーション設定で T ポーズまたはカスタムリギングを使用した場合、モーションが壊れる（上半身が動かない、またはねじれる）。または、指のモーションが正しく適用されない。"
            keywords: ["T pose", "twisted motion", "finger motion", "smoothing"]
            versions: ["2026.6"]
            answer: "これはモーションスムージングシステムのバグが原因です。一時的な回避策として、モーション設定でモーションスムージングを無効にしてください。"
      - title: "📌 バージョン 2026.5 - 2026.6"
        items:
          - id: "model-ik-2026-5-6"
            category: "motion"
            type: "known-issue"
            question: "特定のモデルとモーションで脚が固定位置に向かって引かれている"
            keywords: ["leg position", "IK", "inverse kinematics"]
            versions: ["2026.5", "2026.6"]
            answer: "これは、モーションからIKの動きがない場合にモデル定義のIKが有効になっているためです。回避策：アクターモーション設定から「モデルIK」を無効にしてください。 2026.7リリース以降は不要です。"
---


{% include support-browser.html %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
サポートハブ

## どのようなご用件でしょうか？

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">ドキュメントを参照</h3>
    <p class="support-desc">機能とオプションのガイド</p>
    <a href="features" class="support-cta">ドキュメントを開く</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">トラブルシューティング</h3>
    <p class="support-desc">報告前のチェックリスト</p>
    <a href="troubleshooting" class="support-cta">チェックリストを表示</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">アクティベーション</h3>
    <p class="support-desc">ライセンスキーの管理</p>
    <a href="activation" class="support-cta">アクティベーションガイド</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
お問い合わせ

## バグ報告またはお問い合わせ

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">バグ追跡・機能リクエスト</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">Issueを開く</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">コミュニティサポート</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">Discordに参加</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">メール</h3>
    <p class="support-desc">ビジネス・直接のお問い合わせ</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">メールを送る</a>
  </div>

</div>

</section>