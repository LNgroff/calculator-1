B
    V��^G  �               @   s�  d Z ddlT �x�ed�Ze�d�Zdekr6ed� P nee�dk rLed� qed Zed	 Z	ee�d
k rndZ
ned Z
ee�d
kr�ed
 ZdZe	�� r�e
�� s�ed� q�n(edkr�eee	�ee
��Z�n
edkr�eee	�ee
��Zn�edk�reee	�ee
��Zn�edk�r"eee	�ee
��Zn�edk�r:eee	��Zn�edk�rReee	��Zn�edk�rpeee	�ee
��Zndedk�r�eee	�ee
��ZnFedk�r�eee	�ee
�ee��Zn"edk�r�eee	�ee
��ZndZee� qW dS )z1CLI application for a prefix-notation calculator.�    )�*zEnter your equation > � �qzYou will exit.�   zNot enough inputs.�   �   �0NzThose aren't numbers!�+�-r   �/�square�cube�pow�modzx+zcubes+z2Please enter an operator followed by two integers.)�__doc__Z
arithmetic�inputZ
user_input�split�tokens�print�len�operatorZnum1Znum2Znum3�result�isdigit�add�float�subtractZmultiplyZdivider   r   Zpowerr   Zadd_multZ	add_cubes� r   r   �_meta/calculator.py�<module>   sV   








