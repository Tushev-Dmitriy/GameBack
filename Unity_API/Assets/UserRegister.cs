using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;
using TMPro;
using UnityEngine;
using UnityEngine.Networking;

public class UserRegister : MonoBehaviour
{
    [SerializeField] private TMP_InputField loginField;
    [SerializeField] private TMP_InputField passwordField;
    [SerializeField] private TextMeshProUGUI resultText;
    public string apiUrl = "http://127.0.0.1:8000/register"; // URL ������ �������

    public void RegisterUser()
    {
        StartCoroutine(SendRegistrationRequest());
    }

    private IEnumerator SendRegistrationRequest()
    {
        // ������� JSON-������
        var userData = new UserLoginRequest();
        userData.Login = loginField.text;
        userData.PasswordHash = passwordField.text;

        string jsonData = JsonUtility.ToJson(userData);

        Debug.Log(jsonData);

        // ���������� ������
        UnityWebRequest request = new UnityWebRequest(apiUrl, "POST");
        byte[] bodyRaw = Encoding.UTF8.GetBytes(jsonData);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        // ������������ �����
        if (request.result == UnityWebRequest.Result.Success)
        {
            string responseBody = request.downloadHandler.text;
            UserLoginResponse response = JsonUtility.FromJson<UserLoginResponse>(responseBody);

            // ���������� ���������
            resultText.text = $"����������� �������! �����: {response.Login}";
        }
        else
        {
            Debug.LogError($"������ �����������: {request.error}");
            resultText.text = "������ �����������. ��������� ������.";
        }
    }

}

[System.Serializable]
public class UserLoginResponse
{
    public string Login;
}

[System.Serializable]
public class UserLoginRequest
{
    public string Login;
    public string PasswordHash;
}