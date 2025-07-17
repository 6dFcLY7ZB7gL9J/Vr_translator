using UnityEngine;
using TMPro;
using WebSocketSharp;

public class WebSocketSubtitle : MonoBehaviour {
    public TextMeshProUGUI subtitleText;
    WebSocket ws;

    void Start() {
        ws = new WebSocket("ws://localhost:6789/");
        ws.OnMessage += (s, e) => subtitleText.text = e.Data;
        ws.Connect();
    }

    void OnDestroy() => ws.Close();
}
