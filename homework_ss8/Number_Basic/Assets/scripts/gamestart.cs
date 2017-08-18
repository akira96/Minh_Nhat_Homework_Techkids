using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class gamestart : MonoBehaviour {

	public gamestart.ButtonType bt;

	public gamestart(){
	}

	private void OnMouseDown(){
		transform.localScale = new Vector3 (0.48f,0.48f);
	}

	private void OnMouseUp(){
		transform.localScale = new Vector3 (0.5f,0.5f);
		if (bt == gamestart.ButtonType.btnBasic){
			Application.LoadLevel ("playScene1");
		}
		if (bt == gamestart.ButtonType.btnAdvance){
			Application.LoadLevel ("playScene2");
		}
		if (bt == gamestart.ButtonType.btnBack){
			Application.LoadLevel ("gamestart");
		}
	}
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public enum ButtonType{
		btnBasic,
		btnAdvance,
		btnBack
	}

}
