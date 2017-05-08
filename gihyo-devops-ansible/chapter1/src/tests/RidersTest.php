<?php

use Illuminate\Foundation\Testing\WithoutMiddleware;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class RiderTest extends TestCase
{
    /**
     * @before
     */
    public function setupSeeder()
    {
        $this->artisan('migrate');
        $this->seed();
    }

    /**
     * @test
     */
    public function get_riders_99()
    {
        $this->visit('/riders/99')
             ->seeJson([
                 'no' => '99',
                 'name' => 'Jorge Lorenzo',
             ]);
    }
}
