using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveController : MonoBehaviour
{
    public float speed = 15.0f;
    public float rotateSpeed = 5.0f;

    private CharacterController controller;
    private AudioSource audioSource;
    private bool isDance = false;
    private Animator animator;
    private Vector3 tempPos = Vector3.zero;

    void Start()
    {
        controller = GetComponent<CharacterController>();
        audioSource = Camera.main.GetComponent<AudioSource>();
        animator = GetComponent<Animator>();
    }

    void Update()
    {
        if (!isDance) 
        {
            if (Vector3.Distance(transform.position, tempPos) < 0.01f)
            {
                animator.SetBool("isWalk", false);
            }
            else
            {
                animator.SetBool("isWalk", true);
            }

            float horizontal = Input.GetAxis("Horizontal");
            float vertical = Input.GetAxis("Vertical");

            float mouseX = Input.GetAxis("Mouse X");
            transform.Rotate(Vector3.up, mouseX);

            Vector3 camForward = Camera.main.transform.forward;
            Vector3 camRight = Camera.main.transform.right;
            camForward.y = 0;
            camRight.y = 0;
            camForward.Normalize();
            camRight.Normalize();

            Vector3 movement = camForward * vertical + camRight * horizontal;
            tempPos = transform.position;

            controller.Move(movement * speed * Time.deltaTime);
            transform.position = new Vector3(transform.position.x, 2.69f, transform.position.z);

            if (Input.GetKeyDown(KeyCode.LeftShift))
            {
                speed *= 2;
            }

            if (Input.GetKeyUp(KeyCode.LeftShift))
            {
                speed /= 2;
            }
        }

        if (Input.GetKeyDown(KeyCode.E))
        {
            if (isDance) {
                audioSource.Stop();
                isDance = false;
                animator.Play("Idle");
                animator.SetBool("isDance", false);
                animator.SetBool("isWalk", true);
            }
            else
            {
                audioSource.Play();
                isDance = true;
                animator.SetBool("isWalk", false);
                animator.SetBool("isDance", true);
            }
        }
    }
}