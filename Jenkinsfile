pipeline {
      agent { label 'agent'}

      stages {
             stage('go to directory') {
                steps{
               sh "cd /home/agent/jenkins/jenkins"
                }
             }
             stage('Check code from git') {
                steps{  
             //git config
             git branch: 'main',
             url: 'https://github.com/arman11sargsyan/jenkins.git'
 
                }
             }
             
             stage('build code') {
                steps{
               sh "python3 task3.py > task3_out.txt"
               sh "cat date.txt >> task3_out.txt"
                }
             }

             stage('cat result') {
                steps{ 
               sh "cat task3_out.txt"
                }
             }
      }
}
