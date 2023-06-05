<?php

use App\Http\Controllers\AtestadoApiController;
use App\Http\Controllers\LaudoApiController;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\ReceitaApiController;
use App\Http\Controllers\UserApiController;
use App\Http\Controllers\UserApiController as ControllersUserApiController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::post('token', [LoginController::class, 'login_api']);

Route::prefix('user')->group(function(){
    Route::get('', [UserApiController::class, 'index']);
    Route::post('create', [UserApiController::class, 'store']);
    Route::get('{id}', [UserApiController::class, 'show']);
    Route::post('update/{id}', [UserApiController::class, 'update']);
    Route::delete('delete/{id}', [UserApiController::class, 'destroy']);
});

Route::prefix('atestado')->group(function(){
    Route::get('', [AtestadoApiController::class, 'index']);
    Route::post('create', [AtestadoApiController::class, 'store']);
    Route::get('{id}', [AtestadoApiController::class, 'show']);
    Route::put('update/{id}', [AtestadoApiController::class, 'update']);
    Route::delete('delete/{id}', [AtestadoApiController::class, 'destroy']);
});

Route::prefix('receita')->group(function(){
    Route::get('', [ReceitaApiController::class, 'index']);
    Route::post('create', [ReceitaApiController::class, 'store']);
    Route::get('{id}', [ReceitaApiController::class, 'show']);
    Route::post('update/{id}', [ReceitaApiController::class, 'update']);
    Route::delete('delete/{id}', [ReceitaApiController::class, 'destroy']);
});

Route::prefix('laudo')->group(function(){
    Route::get('', [LaudoApiController::class, 'index']);
    Route::post('post', [LaudoApiController::class, 'store']);
    Route::get('{id}', [LaudoApiController::class, 'show']);
    Route::put('update/{id}', [LaudoApiController::class, 'update']);
    Route::delete('delete/{id}', [LaudoApiController::class, 'destroy']);
});


#Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    #return $request->user();
#});
