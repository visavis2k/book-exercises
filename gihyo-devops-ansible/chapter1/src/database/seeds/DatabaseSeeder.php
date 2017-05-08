<?php

use App\Rider;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Model::unguard();

        $this->ridersSeeder();

        Model::reguard();
    }

    protected function ridersSeeder()
    {
        Rider::updateOrCreate([
            'no' => '99',
            'name' => 'Jorge Lorenzo',
        ]);
        Rider::updateOrCreate([
            'no' => '46',
            'name' => 'Valentino Rossi',
        ]);
        Rider::updateOrCreate([
            'no' => '93',
            'name' => 'Marc Márquez',
        ]);
        Rider::updateOrCreate([
            'no' => '26',
            'name' => 'Dani Pedrosa',
        ]);


    }
}
