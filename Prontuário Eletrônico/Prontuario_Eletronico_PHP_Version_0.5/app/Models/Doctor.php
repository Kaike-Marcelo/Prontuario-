<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Doctor extends Model
{
    use HasFactory;

    protected $fillable = [
        'id',
        'user_id',
        'crm',
        'data_emissao',
        'estado',
    ];

    public function laudo(){
        return $this->hasMany(Laudo::class);
    }

    public function receita(){
        return $this->hasMany(Receita::class);
    }

    public function atestado(){
        return $this->hasMany(Atestado::class);
    }
}
