import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from '../core/auth.service';

@Component({
  selector: 'app-docente',
  imports: [CommonModule],
  templateUrl: './docente.html',
  styleUrl: './docente.css',
})
export class DocenteComponent {
  constructor(public auth: AuthService) {}

  voti:any[] = [];

}