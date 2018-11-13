## Soru İsmi: Signal

## Soru Metni: 

Soruda verilen dosya: [Signal.apk](Signal.apk)

## Çözüm: 

Apk decompile edildiğinde görülen

- intent.setAction("ctf.stm.com.FLAG_INFO");
- sendBroadcast(intent);

Satırları uygulamanın bir broadcast yaptığını gösteriyor. Broadcastı dinleyen bir uygulama yazılarak Flag elde edilebilir.

İkinci bir yöntem ise decompile sonucunda elde edilen kodu takip ederek stringleri doğru şekilde birleştirip doğru sayıda decode etmek.

Örnek kod: 
```
public class MyReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        System.out.println(intent.getExtras().get("flag"));
    }
}
```
```
<receiver android:name=".MyReceiver" android:exported="true">
<intent-filter>
<action android:name="ctf.stm.com.FLAG_INFO"/>
</intent-filter>
</receiver>
```

Flag: STMCTF{Nerede_Eski_Radyolar}
