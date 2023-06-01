<?php

namespace App\Http\Controllers;

use App\Models\Doctor;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class LoginController extends Controller
{
    public function login_api(Request $request){

        $data = $request->all();

        
        $user = User::where('email', $data['email'])->first();

        if(!$user || !Hash::check($data['password'], $user->password) || !$user->doctor){
            return response(['message'=> 'Usuario ou senha invalida'], 401);
        }

        $doctor = $user->doctors;

        $token = $user->createToken($user) -> plainTextToken;

        $response = [
            'user'=> $user,
            'doctor' => $doctor, 
            'token'=> $token
        ];

        return response($response, 201);

    }
}
