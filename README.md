# 北大期末教學意見調查自動填表 (AUTO NTPU Teaching Assessment Questionnaire)

簡單實現了一個可以自動填期末意見調查表的東西，會用到的套件在`requirements.txt`裡面
相應檔案的雲端硬碟連結:
https://drive.google.com/drive/folders/1fz2w76UiQMEXRLDl9kfTr7oVxfrEr5qZ?usp=drive_link
其餘操作如下，和連結內的`README.txt`基本一致

## 前言
這東西是我上課上到很無聊做的 所以問題一堆 程式寫的很醜實作方法也很爛 主要只是要能用 使用上有問題請果斷關掉重開
用這個填的話除了兩題陷阱題是填一分 其他題都是80趴機率填5然後20趴機率填4 回饋都是回 ‘謝謝老師！’ 有疑慮或想客製回覆的跟我講我再改改
打開之後可能要等他個幾秒才會有東西跑出來

## 使用步驟

### Step1 
把這個repo clone到你的電腦

### Step2 
如果你的電腦裡面沒有火狐的話打開火狐那個(`Firefox Installer.exe`) 照著他的提示走 他會幫你裝一個火狐 已經裝過了的話就不用

### Step3.1 
打開圖標是以前系學會頭貼的那個小程式(`填表小程式_113.exe`) 他說這個程式有危險的話不要管他 跑下去就對了 這沒有毒相信我
### Step3.2 
打你的學號按Enter 因為實作上的一些小偷懶，所以這裡按完Enter應該會卡一下，麻煩請等他一下，如果不小心按了第二次Enter的話請果斷重開，這裡我沒寫好啦但等他一下的話還算能用 然後打你的密碼按Enter

### Step4 
然後這東西是在你的電腦上跑的 我也沒寫什麼能存東西或傳東西的功能 所以不用擔心密碼的問題

### Step5 
理論上應該已經開始跑了 出現登入中 請稍候之後可能要等他一下 有跑了就放著等他 然後看**Step7** 沒跑的話請看**Step6**

### Step6.1 
沒跑的話主要有兩個可能，一個是 `填表小程式_113.exe` 跟 `geckodriver.exe
` 不在同一個資料夾，請去檢查並確認兩個檔在同一個資料夾內後回到**Step3**重來
### Step6.2 
另一個可能是你的 `firefox.exe` 安裝的位置跟我猜的不一樣 請找到你的 `firefox.exe` 在你電腦的哪裡，然後把路徑照著提示輸進去，通常是像 `C:/Program Files/Mozilla Firefox/firefox.exe` 這種格式 (注意斜線方向，請盡量不要用反斜線\)，接著按Enter然後看他有沒有正常跑，還是不能用的話請來找我我來看看。

### Step7 
慢慢等他跑完之後去你的學生資訊系統檢查一下是不是填完了 如果出bug有幾個還沒填完 麻煩回到**Step3**再重跑一次 還是不行的話麻煩來密我

### Step8 
理論上已經完成了 太棒啦
